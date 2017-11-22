#!/usr/bin/env python
# -*- coding:utf-8 -*-
# arthur:Dear
# 2017-11-21 10:41:47


import asyncio


class Crawl:
    '''
    爬取一个连接的所有图片信息和url并保存
    '''
    def __init__(self, reository, htmlhandler, downloader, parser):
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
        response = await self.htmlhandler.get(url)
        data = Parser(response).parse_all()
        asyncio.ensure_future(self.fetch_completed(data))
        return data

    async def fetch_completed(self, data):
        '''爬取完成后的操作,将爬取到的数据保存到数据库, 并下载图片保存到本地磁盘

        Args:
            data: 需要保存的信息, 字典类型
        '''
        await self.reository.put(data, table)
        await self.downloader.down(data['pictures'])


if __name__ == '__main__':
    reository = Reository()
    htmlhandler = HtmlHandler()
    downloader = DownLoader()
    crawl = Crawl(reository, htmlhandler, downloader)
