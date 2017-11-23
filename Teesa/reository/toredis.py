#!/usr/bin/env python
# -*- coding:utf-8 -*-
# arthur:Dear
# 2017-11-23 09:55:21

import aioredis

import settings

class TORedis:
    def __init__(self, setting):
        self.conn = self.connection(setting['host'])

    def connection(self, host, *, port=6379, password=None, db=0):
        pass
        return conn

    def insert(self, data):
        pass

    def delete(self, data):
        pass
