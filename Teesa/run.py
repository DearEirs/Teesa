import asyncio

import scheduler
import crawler
from reository import *
import settings
from handler import html
import downloader


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    downloader = downloader.Downloader()
    htmlhandler = html.HtmlHandler(loop)
    conn = tomysql.TOMysql(settings['MYSQL_CONFIG'])
    reository = reository.Reository(conn)
    conn = tomysql.TORedis(settings['REDIS_CONFIG'])
    cache = reository.Reository(conn)
    crawl = crawler.BaseCrawl(reository, htmlhandler, downloader, cache)
    scheduler = scheduler.Scheduler(crawl)
    scheduler.run()
