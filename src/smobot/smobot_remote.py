import aiohttp
import json
import asyncio


class SmobotRemote:
    def __init__(self, ip, id, username, password):
        self.ip = ip
        self.id = id
        self.username = username
        self.password = password
        self._base_url = f"http://mysmobot.com/secureapi/"
        self._headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Encoding": "gzip, deflate",
            "Accept-Language": "en-us",
        }
        cookies = {"cookies_are": "JSESSIONID"}
        self.session = aiohttp.ClientSession(cookies=cookies)

    async def close(self):
        await self.session.close()

    async def login(self):
        print(self.session.cookie_jar)
        path = f"smobot/login"
        body = {"username": self.username, "password": self.password}
        async with self.session.post(
            self._base_url + path, json=body, headers=self._headers
        ) as response:
            resp = await response.json()
            cookies = response.cookies
            print(resp)
            print(cookies)
            response.raise_for_status()
            self._headers["X-Auth-Token"] = resp["access_token"]

    async def get_status(self):
        path = f"smobot/current/{self.id}.json"
        status = await self.get(path)
        print(status)

    async def get(self, path):
        async with self.session.get(self._base_url + path) as response:
            return await response.json()
