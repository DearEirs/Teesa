import asyncio

from settings import SCHEDULER


class Scheduler:
    async def get_url(self, q):
        url = await self.q.get()
        return url

    async def push_url(self, url, downloader):
        resp = await downloader.down(url)
        return resp

    def run(self):
        if not SCHEDULER.stopped:
            asyncio.ensure_future(self.get_url())

    def stop(self):
        pass
