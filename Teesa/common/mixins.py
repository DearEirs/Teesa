# from parser import JsonParser, XMLParser, HTTPParser

# TYPE_TO_PARSER = {
#    'json': JsonParser,
#    'xml': XMLParser,
#    'http': HTTPParser,
# }

class UrlNormalizationMixin:
    def url_normal(self, url):
        return url


class HeaderSetterMixin:
    def set_header(self, header):
        self.header = header
        return self.header

    def get_header(self, url):
        pass
        return header


class SeedExtractorMixin:
    def extract(self, response):
        return seeds


class DataExtractorMixin:
    def extract(self, response):
        return data


class DistributorMixin:
    def distribute(self, response):
        type = self.check_response(response)
        parser = TYPE_TO_PARSER(type)
        data = parser.parse(response)
        return data

    def check_response(self, response):
        return type
