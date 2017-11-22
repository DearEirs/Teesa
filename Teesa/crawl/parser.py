#!/usr/bin/env python
# -*- coding:utf-8 -*-
# arthur:Dear
# 2017-11-22 14:53:24

import Resolver

class Parser:
    def __init__(self, response):
        self.reponse = response
        self._parse_url(response)

    def parse(self, response):
        '''根据获取到的网页内容, 筛选自己所需要的信息

        Args:
            response: 需要爬取的页面内容

        Returns:
            一个字典, 包含图片基本信息, 例子如下:
            {'id': '123',
            'title': 'test',
            'url': 'http://www.poco.cn',
            'pictures': ['http://www.poco.cn/images/Square-images/btn-r-49x85.png',
                        'http://image170-c.poco.cn/mypoco/myphoto/20171120/09/2376023820171120094446012.jpg']
            }
        '''
        response = Resolver(response).to_xpath()
        urls = self.parse_url(response)
        data = self.parse_data(response)
        data = {}
        pass
        return data

    def parse_url(self):
        pass

    def parse_all(self):
        self.parse_url()
