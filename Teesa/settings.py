import sys
import os

sys.path.append(os.getcwd())

MYSQL_CONFIG = {
    'host': '127.0.0.1',
    'port': '3306',
    'db': 'tessa',
    'user': 'tessa',
    'password': 'password'
}

REDIS_CONFIG = {
    'host': '127.0.0.1',
    'port': '3306'
}
