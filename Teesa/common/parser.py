import json
from lxml import etree


def parse_html(response):
    response = etree.HTML(response)
    return response


def parse_json(data):
    data = json.dumps(response)


def parse_xml(response):
    pass
