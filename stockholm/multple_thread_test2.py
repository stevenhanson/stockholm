"""
通过继承threading.Thread来实现多线程
"""
import threading
import time


class CodingThread(threading.Thread):
    def run(self):
        for i in range(3):
            print("正在编码%s" % threading.currentThread())
            time.sleep(1)


class DrawingThread(threading.Thread):
    def run(self):
        for i in range(3):
            print("正在画画%s" % threading.currentThread())
            time.sleep(1)


if __name__ == '__main__':
    t1 = CodingThread()
    t2 = DrawingThread()

    t1.start()
    t2.start()
