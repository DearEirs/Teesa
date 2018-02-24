import sys



sys.path.append('/data/python/Teesa/Teesa')
QUEUE = {
    'maxsize': 10000
}

DOWNLOADERS = ['127.0.0.1:9002']

DOWNLOADERS = ['http://' + host + '/downloader/put' for host in DOWNLOADERS]

SCHEDULER = {
    'enabled': True
}
