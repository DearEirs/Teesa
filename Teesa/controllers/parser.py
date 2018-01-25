from parser import JsonParser, XMLParser, HTTPParser


class Parser:
    def __init__(self):
        self.TYPE_TO_PARSER = {
            'json': JsonParser,
            'xml': XMLParser,
            'http': HTTPParser,
        }

    def _distribute(self, response):
        type = self._check_response(response)
        parser = self.TYPE_TO_PARSER(type)
        return parser

    def _check_response(self, response):
        type = 'http'
        return type

    def parse(self, response):
        _parser = self._distribute(response)
        data = _parser.parse(response)
        return data
