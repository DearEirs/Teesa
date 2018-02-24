import asyncio
import uvloop
import random

import config
from common.httprequest import async_request


class Scheduler:
    def __init__(self):
        self.q = None

    async def get(self, q=None):
        seed = await self.q.get()
        return seed

    async def put(self, seed):
        result = await self.q.put(seed)
        return result

    async def dispatch(self, data, downloader):
        resp = await async_request(downloader, params=data, method='post')
        return

    async def schedule(self):
        while config.SCHEDULER['enabled']:
            seed = await self.get()
            downloader = random.choice(config.DOWNLOADERS)
            resp = await self.dispatch(seed, downloader)

    async def start(self, loop):
        if not self.q:
            await self.__init_queue(loop)
        asyncio.ensure_future(self.schedule())
        return {"result": "True"}

    def stop(self):
        config.SCHEDULER['enabled'] = False
        return True

    async def __init_queue(self, loop):
        self.q = asyncio.Queue(maxsize=config.QUEUE['maxsize'], loop=loop)
        return self.q

    def health(self):
        pass

    async def count(self):
        l = await self.q.qsize()
        return l

