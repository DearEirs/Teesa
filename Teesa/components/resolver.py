#!/usr/bin/env python
# -*- coding:utf-8 -*-
# arthur:Dear
# 2017-11-22 16:26:52

from lxml import etree


class ResolverMixin:
    def __init__(self, response):
        self.response = response

    def resolve_to_xpath(self):
        return etree.HTML(self.response)

    def resolve_to_bs4(self):
        pass
