import asyncio

import settings
from controllers import Scheduler, Downloader, Parser, Extractor, Deduplicator, Saver


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    scheduler = Scheduler()
    asyncio.ensure_future(scheduler.run())




    mysql_conn = tomysql.TOMysql(settings['MYSQL_CONFIG'])
    repository = repository.repository(mysql_conn)
    redis_conn = tomysql.TORedis(settings['REDIS_CONFIG'])
    cache = repository.repository(redis_conn)

    parser = Parser()
    downloader = downloader.Downloader()
    extractor = Extractor()
    deduplicator = Deduplicator()

    url = scheduler.get_url()
    response = downloader.down(url)
    response = parser.parse(response)
    seed = extractor.extract_seed(response)
    data = extractor.extract_data(response)
    seed = deduplicator.check(seed)
    data = deduplicator.check(data)

    loop.run_forever()
