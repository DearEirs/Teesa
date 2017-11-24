from common.counter import Counter


class HtmlHandleMixin:
    def __init__(self, loop):
        self.loop = loop

    @Counter.add
    async def get(self, url):
        '''异步打开网页

        Args:
            url: 字符串类型,必须是可打开的网页链接,如:
            'http://www.poco.cn'

        '''
        async with aiohttp.ClientSession(loop=self.loop) as session:
            async with session.get(url) as response:
                response = await response.read()
                return response

