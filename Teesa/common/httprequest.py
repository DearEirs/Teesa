import aiohttp
import json

import settings


methods = ['GET', 'POST', 'PUT', 'DELETE', 'get', 'post', 'put', 'delete']


async def async_request(url, header=settings.HEADER, params=None, method='GET'):
    if method not in methods:
        return {'message': 'InvalidMethod: %s' % method}
    async with aiohttp.ClientSession() as session:
        async with session.request(method, url, data=json.dumps(params)) as response:
            response = await response.read()
            return response
