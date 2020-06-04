"""Testscript for smobot dev"""
import aiohttp
import json
import asyncio

from smobot import Smobot


async def main(config):
    smobot = Smobot(config["ip"])
    # login
    # await smobot.update_status()
    print(await smobot.status)

    # close
    await smobot.close()


if __name__ == "__main__":
    with open("tests/config.json") as f:
        config = json.load(f)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(config))
