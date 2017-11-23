import asyncio


class BaseCrawl(ParserMixin, HtmlHandleMixin):
    '''
    爬取一个连接的所有图片信息和url并保存
    '''
    def __init__(self, reository, downloader, cache):
        pass

    async def fetch(self, url):
        '''爬取一个连接的所有图片信息
        Args:
            url: 需要爬取的连接, 字符串类型

        Returns:
            一个字典, 包含图片基本信息, 例子如下:
            {'id': '123',
             'title': 'test',
             'url': 'http://www.poco.cn',
             'pictures': ['http://www.poco.cn/images/Square-images/btn-r-49x85.png',
                          'http://image170-c.poco.cn/mypoco/myphoto/20171120/09/2376023820171120094446012.jpg']}
        '''
        response = await self.get(url)
        urls, data = self.parse(response)
        asyncio.ensure_future(self.fetch_completed(urls, data))
        return urls, data

    async def fetch_completed(self, urls, data):
        '''爬取完成后的操作,将爬取到的数据保存到数据库, 并下载图片保存到本地磁盘

        Args:
            data: 需要保存的信息, 字典类型
        '''
        await self.cache.insert(urls)
        await self.reository.put(data)
        await self.downloader.down(data['pictures'])
