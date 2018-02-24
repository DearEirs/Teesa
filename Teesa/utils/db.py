import asyncio

import aiomysql
import aioredis

from settings import MYSQL, REDIS, QUEUE


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
    def __init__(self):
        self._r = BaseRedis()
        self._pool = self._r.get_redis_pool()

    async def execute_command(self, command, key, value=None):
        conn = await self._pool
        result =  await conn.execute(command, key, value)
        return result

    async def insert(self, data):
        result = await self.execute_command('sadd', 'urls', data)
        pass

    async def delete(self, data):
        pass

    async def get_seed(self):
        pass

    async def set_seed(self):
        pass

    async def get_rule(self, type, id):
        rule = await self.execute_command('hget', type, id)
        return rule

    async def set_rule(self, type, id, rule):
        await self.execute_command('hset', type, id, rule)

    async def set_rules(self, type, id, rule):
        pass

    async def close(self):
        await self._pool.close()



class BaseRedis:
    async def get_redis_pool(self):
        if not self._pool:
            self._pool = await asyncio_redis.Pool.create(
                host=str(REDIS_DICT.get('REDIS_ENDPOINT', "localhost")), port=int(REDIS_DICT.get('REDIS_PORT', 6379)),
                poolsize=int(REDIS_DICT.get('POOLSIZE', 10)), password=REDIS_DICT.get('REDIS_PASSWORD', None),
                db=REDIS_DICT.get('DB', None)
            )
        return self._pool

    async def get_redis_client(self):
        if not self._pool:
            self.get_redis_pool()
        client = await self._pool()
        return client

