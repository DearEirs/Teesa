from mixins import ResponseDistributorMixin, JsonParser, XMLParser, HTMLParser
from parser import ResponseDistributor

class Parser:

    def parse(self, response):
        data = ResponseDistributor.distribute(response)
        return data


