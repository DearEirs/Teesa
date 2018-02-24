import sys



sys.path.append('/data/python/Teesa/Teesa')
QUEUE = {
    'maxsize': 10000
}

SAVER = ['127.0.0.1:9002']

SAVER = [host + '/downloader/put' for host in SAVER]

DOWNLOADER = {
    'enabled': True

}

HEADERS = {}
