#!/usr/bin/env python

from recomment_portrait.portraitRpc import OctinnPortraitThrift
from recomment_portrait.portraitRpc.ttypes import *
from recomment_portrait.portraitRpc.constants import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
import socket


class HelloWorldHandler:
    def __init__(self):
        self.log = {}

    def getUserProfile(self, user_id):

        return UserProfileT()

    def getUserBehavior(self, user_id):

        return UserBehaviorT()

    def getUserContext(self, user_id):

        return UserContextT()

    def getGoodPortrait(self, good_id):

        return GoodPortraitT()

handler = HelloWorldHandler()
processor = OctinnPortraitThrift.Processor(handler)
transport = TSocket.TServerSocket('localhost', 5002)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

print "Starting python server..."
server.serve()
print "done!"

