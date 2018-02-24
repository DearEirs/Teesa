import sys
import os


sys.path.append(os.getcwd())

MYSQL = {
    'host': '127.0.0.1',
    'port': '3306',
    'db': 'tessa',
    'user': 'tessa',
    'password': 'password'
}

REDIS = {
    'host': '127.0.0.1',
    'port': '3306'
}

HEADER = {
    'Content-Type': 'application/json'
}

QUEUE = {
    'maxsize':10000
}
