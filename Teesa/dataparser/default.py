#!/usr/bin/env python
# -*- coding:utf-8 -*-
# arthur:Dear
# 2017-11-23 10:22:28

class DataParserMinix:
    def get_data(self, response):
        '''爬取页面所需数据
        Args:
            response: 待爬取的网页内容, 已经通过Resolver解析成可用xpath的格式

        Returns:
            一个字典, 包含图片基本信息, 例子如下:
            {'id': '123',
            'title': 'test',
            'url': 'http://www.poco.cn',
            'pictures': ['http://www.poco.cn/images/Square-images/btn-r-49x85.png',
                        'http://image170-c.poco.cn/mypoco/myphoto/20171120/09/2376023820171120094446012.jpg']}
        '''
        pass
        return data
