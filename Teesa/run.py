import asyncio

import crawler
import downloader
import settings
import scheduler
from reository import *


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    downloader = downloader.Downloader()
    conn = tomysql.TOMysql(settings['MYSQL_CONFIG'])
    reository = reository.Reository(conn)
    conn = tomysql.TORedis(settings['REDIS_CONFIG'])
    cache = reository.Reository(conn)
    crawl = crawler.BaseCrawl(reository, downloader, cache)
    scheduler = scheduler.Scheduler(crawl)
    scheduler.run()
