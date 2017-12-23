from parser import JsonParser, XMLParser, HTTPParser


TYPE_TO_PARSER = {
    'json': JsonParser,
    'xml': XMLParser,
    'http': HTTPParser,
}

class ResponseDistributor:
    def distribute(self, response):
        type = self.check_response(response)
        parser = TYPE_TO_PARSER(type)
        data = parser.parse(response)
        return data
