#!/usr/bin/env python
# -*- coding:utf-8 -*-
# arthur:Dear
# 2017-11-21 14:14:44


class Reository:
    def __init__(self, conn):
        self.conn = conn

    def put(self, data, table):
        return self.conn.insert(data)

    def delete(self, id, table):
        return self.conn.delete(id)

    def find_by_id(self, id, table):
        return self.conn.select(id)

    def get_url(self):
        return self.conn.get_seed()
