======
smobot
======

Python package to interface with the [Smobot](http://smobot.com/) device using asynchronous http (aiohttp).


Description
===========

Currently only implements the local api, which just needs a IP address.

```Python
import asyncio
from smobot import Smobot

async def main(ip):
    smobot = Smobot(ip)
    print(await smobot.status)
    await smobot.close()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete('192.168.4.1')

```


Note
====

This project has been set up using PyScaffold 3.2.3. For details and usage
information on PyScaffold see https://pyscaffold.org/.
