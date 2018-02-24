from common.parser import parse_html, parse_json, parse_xml
from extractor import Extractor


class Parser:
    def __init__(self):
        self.e = Extractor()
        self.TYPE_TO_PARSE = {
            'json': parse_json,
            'xml': parse_xml,
            'html': parse_html,
        }

    async def parse(self, seed):
        _parse = self.TYPE_TO_PARSE(seed['type'])
        response  = _parse(seed['response'])
        await self.e.extract(seed)
        return response
