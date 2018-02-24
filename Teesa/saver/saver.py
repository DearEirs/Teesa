class Saver:
    async def save_data(self, data, conn):
        result = await self.conn.insert(data)
        return result

    async def save_seed(self, seeds, q):
        for seed in seeds:
            await q.put(seed)
