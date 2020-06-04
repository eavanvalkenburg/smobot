"""File with class for Local Smobot."""
import aiohttp
import json
import asyncio
import time

from .smobot_status import SmobotStatus


class Smobot:
    """Class for talking with Smobot Locally."""

    def __init__(self, ip: str):
        """Create the smobot client.

        Arguments:
            ip {string} -- ip address of the Smobot.
        """
        self._ip = ip
        self._base_url = f"http://{self._ip}/ajax/"
        self._headers = {
            "Accept": "*/*",
            "Content-Type": "application/json",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-us",
        }
        self.session = aiohttp.ClientSession(
            headers=self._headers, raise_for_status=True
        )
        self._status = None

    async def close(self):
        """Close the session."""
        return await self.session.close()

    @property
    async def status(self):
        """Get status."""
        if not self._status:
            await self.update_status()
        return self._status

    async def update_status(self):
        """Update the status of your smobot."""
        async with self.session.get(self._base_url + "smobot") as response:
            full_state = await response.json()
            print(full_state)
            self._status = SmobotStatus(**full_state)

    async def post_setpoint(self, setpoint):
        """Set the setpoint for the smobot."""
        body = {"setpoint": setpoint}
        async with self.session.post(
            self._base_url + "setgrillset", json=body
        ) as response:
            return await response.json()
