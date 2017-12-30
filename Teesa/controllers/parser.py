from common.mixins import ResponseDistributorMixin
from parser import ResponseDistributor

class Parser(ResponseDistributorMixin):

    def parse(self, response):
        _parser = self.distribute(response)
        data = _parser.parse(response)
        return data


