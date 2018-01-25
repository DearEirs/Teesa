import asyncio

import aiomysql
import aioredis

from settings import MYSQL, REDIS, QUEUE


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


class Mysql:
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


class Redis:
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


queue = asyncio.Queue(QUEUE.maxsize)
