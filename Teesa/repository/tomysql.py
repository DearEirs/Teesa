#!/usr/bin/env python
# -*- coding:utf-8 -*-
# arthur:Dear
# 2017-11-23 09:42:00

import aiomysql

import settings


class TOMysql:
    def __init__(self, setting):
        self.conn = self.connection(setting['host'], setting['user'],
                                    setting['password'], setting['db'])

    def connection(self, host, user, password, db, *, port=3306):
        pass
        return conn

    def insert(self, data):
        pass

    def delete(self, id):
        pass

    def select(self, id):
        pass
