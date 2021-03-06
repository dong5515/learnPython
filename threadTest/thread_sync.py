#!/usr/bin/python
# -*- coding: utf-8 -*-

import threading
import time

class myThread (threading.Thread):
    def __init__(self, threadID, name, cnt):
	threading.Thread.__init__(self)
	self.threadID = threadID
	self.name = name
 	self.cnt = cnt
    def run(self):
	print "Starting " + self.name
	# 获得锁
	threadLock.acquire() 
	print_time(self.name, self.cnt, 5)
	# 释放锁
	threadLock.release()

def print_time(threadName, delay, cnt):
    while cnt:
	time.sleep(delay)
	print "%s: %s" % (threadName, time.ctime(time.time()))
	cnt -= 1

threadLock = threading.Lock()
threads = []

# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成
for t in threads:
    t.join()
print "Exiting Main Thread"

