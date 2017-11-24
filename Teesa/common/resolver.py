#!/usr/bin/env python
# -*- coding:utf-8 -*-
# arthur:Dear
# 2017-11-22 16:26:52

from lxml import etree


class Resolver:
    def __init__(self, response):
        self.response = response

    def to_xpath(self):
        return etree.HTML(self.response)

    def to_bs4(self):
        pass
