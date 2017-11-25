import asyncio

import settings
from repository import *
from common import downloader
from controllers import crawler
from controllers import scheduler


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    downloader = downloader.Downloader()
    mysql_conn = tomysql.TOMysql(settings['MYSQL_CONFIG'])
    repository = repository.repository(mysql_conn)
    redis_conn = tomysql.TORedis(settings['REDIS_CONFIG'])
    cache = repository.repository(redis_conn)
    crawl = crawler.BaseCrawl(repository, downloader, cache)
    scheduler = scheduler.Scheduler(crawl)
    scheduler.run()
