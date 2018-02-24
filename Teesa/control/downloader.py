import asyncio

import config
from common.httprequest import async_request
from common.mixins import HeaderSetterMixin, UrlNormalizationMixin
from parser import Parser


class Downloader(HeaderSetterMixin, UrlNormalizationMixin):
    def __init__(self):
        self.q = None
        self.p = Parser()

    async def down(self, url, header=None):
        url = self.url_normal(url)
        default_header = config.HEADERS
        header = default_header.update(header) if header else default_header
        response = await async_request(url, header)
        return response

    async def start(self, loop):
        if not self.q:
            await self.__init_queue(loop)
        asyncio.ensure_future(self.__run_forever())

    def stop(self):
        config.DOWNLOADER['enabled'] = False
        return True

    async def __init_queue(self, loop=None):
        self.q = asyncio.Queue(maxsize=config.QUEUE['maxsize'], loop=loop)
        return self.q

    async def put(self, url):
        result = await self.q.put(seed)
        return result

    async def __run_forever(self):
        while config.DOWNLOADER['enabled']:
            seed = await self.q.get()
            seed = json.dumps(seed)
            seed['response'] = await self.down(seed['url'])
            result = await self.p.parse(seed)
