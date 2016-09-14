#!/usr/bin/env python
# -*- coding:utf-8 -*-


from recommend_server import OctinnRecommendThrift
from recommend_server.ttypes import *
from recommend_server.constants import *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
import time
import threading
from time import sleep
import random


# 配置:模拟运行状态
THREAD_NUM = 1       # 并发线程总数
ONE_WORKER_NUM = 1     # 每个线程的循环次数
LOOP_SLEEP = 0.5        # 每次请求时间间隔(秒)

# 出错数
ERROR_NUM = 0


def test_portrait_server(index):
    t = threading.currentThread()
    try:
        # Make socket
        transport = TSocket.TSocket('localhost', 5000)

        # Buffering is critical. Raw sockets are very slow
        transport = TTransport.TBufferedTransport(transport)

        # Wrap in a protocol
        protocol = TBinaryProtocol.TBinaryProtocol(transport)

        # Create a client to use the protocol encoder
        client = OctinnRecommendThrift.Client(protocol)

        # Connect!
        transport.open()
        user_id = random.randint(0, 5760000)
        recommendtype = RecommendTypeT()
        context = UserContextT()

        user_profile = client.recommendGoods(recommendtype.VIEW_THEN_VIEW, context.page, 1000, 10)

        print user_profile
        transport.close()
    except Thrift.TException, tx:
        print "[" + t.name + " " + str(index) + "] "
        print "%s" % tx.message
        global ERROR_NUM
        ERROR_NUM += 1


def working():
    t = threading.currentThread()
    print "[" + t.name + "] Sub Thread Begin"
    i = 0
    while i < ONE_WORKER_NUM:
        i += 1
        test_portrait_server(i)
        sleep(LOOP_SLEEP)

    print "[" + t.name + "] Sub Thread End"


def main():
    # test_portrait_server(0)
    # return

    t1 = time.time()

    threads = []

    # 创建线程
    for i in range(THREAD_NUM):
        t = threading.Thread(target=working, name="T" + str(i))
        t.setDaemon(True)
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print "main thread end"

    t2 = time.time()
    print "========================================"
    print "任务数量:", THREAD_NUM, "*", ONE_WORKER_NUM, "=", THREAD_NUM * ONE_WORKER_NUM
    print "总耗时(秒):", t2 - t1
    print "每次请求耗时(秒):", (t2 - t1) / (THREAD_NUM * ONE_WORKER_NUM)
    print "每秒承载请求数:", 1 / ((t2 - t1) / (THREAD_NUM * ONE_WORKER_NUM))
    print "错误数量:", ERROR_NUM


if __name__ == "__main__":
    main()

