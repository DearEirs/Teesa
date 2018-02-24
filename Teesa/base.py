class BaseHandler:
    def __init__(self):
        self.q = None
    
    async def dispatch(self, data, url, method='get'):
        resp = await async_request(downloader, params=data, method='post')
        return resp
    
    def health(self):
        pass
    
    async def get(self, q=None):
        data = self.q.get()
        return data

    async def put(self, data, q=None):
        result = await self.q.put(data)
        return result

    async def count(self):
        l = await self.q.qsize()
        return l
    
    
