import os
import time

import multiprocessing

from multiprocessing import Pool,Process
from random import random
from multiprocessing import Queue

'''
线程状态：新建，就绪，运行，阻塞，结束
一个线程sleep后，变成阻塞，sleep结束后，变成就绪；线程无明确执行顺序
'''
import threading

def dosth():
    pass

if __name__ == '__main__':
    threading.Thread(target=dosth,name="",args=(1,))
# def download(q):
#     files = ["jpg","zip","exe"]
#     for file in files:
#         print("downloading :" ,file)
#         time.sleep(1)
#         q.put(file)
# def getfile(q):
#     downloaded_file = []
#     while True:
#         file = q.get(timeout=5)
#         print("get file : " ,file)
#         downloaded_file.append(file)
#
# if __name__ == '__main__':
#     q = Queue(5)
#     p1 = Process(target=download,args=(q,))
#     p2 = Process(target=getfile,args=(q,))
#     p1.start()
#     p2.start()
# def single_task(job):
#     start = time.time()
#     print("begin")
#     print("begin job : %s , the pid is %d" %(job, os.getpid()))
#     time.sleep(random() * 20)
#     end = time.time()
#     print("job ： {1}finished : {0}".format(job, end - start))
#
#
# if __name__ == '__main__':
#     print("begin job : %s , the pid is %d".format("job", os.getpid()))
#     pool = Pool(5)
#     jobs = ["print", "act", "play", "do", "kick", "touch"]
#     for j in jobs:
#         pool.apply_async(func=single_task, args=(j,))
#     pool.close()
#     pool.join()
#     q = Queue(4)
#     q.put("1")
#     q.put("2")
#     if not q.full():
#         q.put(3)
#         print(q.qsize())
#     print(q.get())

#
# def task1():
#     while True:
#         time.sleep(1)
#         print("taks1--------")
#
# def task2():
#     while True:
#         time.sleep(1)
#         print("taks2--------")
#
# if __name__ == '__main__':
#     p1 = multiprocessing.Process(target=task1,name="tt1")
#     p2 = multiprocessing.Process(target=task2)
#     p1.start()
#     p2.start()
#
# t = time.time()
# print(t)
# s = time.ctime(t)
# print(s)
# s = time.strftime("%Y/%m")
# print(s)
# s = time.strptime("2020","%Y")
# print(s)
# print(s.tm_min)
# print(time.localtime().tm_hour)
#
#
# import datetime
# d = datetime.date(2020,3,3)
# print(datetime.date.ctime(d))
#
#
# import hashlib
#
# h = hashlib.md5("abc".encode("utf-8"))
# print(h)
# print(h.hexdigest())
