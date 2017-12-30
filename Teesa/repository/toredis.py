#!/usr/bin/env python
# -*- coding:utf-8 -*-
# arthur:Dear
# 2017-11-23 09:55:21

import aioredis


class TORedis:
    def __init__(self, setting):
        self.pool = await aioredis.create_pool(setting.REDIS_URL)

    def execute_command(self, command, key, value=None):
        with await pool as conn:
            result =  await conn.execute(command, key, value)
            return result

    def insert(self, data):
        result = await self.execute_command('sadd', 'urls', data)
        pass

    def delete(self, data):
        pass

    def get_seed(self):
        self.conn.

    def close(self):
        self.pool.close()
        await self.pool.close()
