"""Service backend"""
import os
import sys
import json
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer
from bson.json_util import dumps
import operations
#import utils packages
sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))

import mongodb_client  
SERVER_HOST = 'localhost'
SERVER_PORT = 4040

def add(num1, num2):
    """Test method"""
    print("Add is called with %d and %d" % (num1, num2))
    return num1 + num2


def get_one_news():
    """Get one news"""
    print("get_one_news is called")
    news = mongodb_client.get_db()['tap-news'].find_one()
    return operations.getOneNews()


RPC_SERVER = SimpleJSONRPCServer((SERVER_HOST, SERVER_PORT))
RPC_SERVER.register_function(add, 'add')
RPC_SERVER.register_function(get_one_news, 'getOneNews')


print("starting rpc server on %s:%d" % (SERVER_HOST, SERVER_PORT))

RPC_SERVER.serve_forever()
