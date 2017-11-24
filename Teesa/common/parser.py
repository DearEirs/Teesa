from libs import Resolver
import DataParserMixin

class ParserMixin(DataParserMixin):
    def __init__(self, response):
        self.reponse = response

    def parse(self, response):
        '''根据获取到的网页内容, 筛选自己所需要的信息

        Args:
            response: 需要爬取的页面内容

        Returns:
            urls: 列表, 包含网站内所有链接
            data:
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
        return urls, data

    def parse_url(self, response):
        '''爬取页面所有url'''
        return urls

    def parse_data(self, response):
        '''爬取页面所需数据'''
        data = self.get_data(response)
        return data
