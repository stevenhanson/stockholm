"""
多线程
"""
import time
import threading

# 传统方式执行
# def coding():
#     for i in range(3):
#         print("正在写代码%s" % i)
#         time.sleep(1)
#
#
# def drawing():
#     for i in range(3):
#         print("正在画画%s" % i)
#         time.sleep(1)
#
#
# coding()
# drawing()


# 使用多线程执行
def coding():
    for i in range(3):
        print("正在写代码%s" % i)
        time.sleep(1)


def drawing():
    for i in range(3):
        print("正在画画%s" % i)
        time.sleep(1)


def main():
    t1 = threading.Thread(target=coding)
    t2 = threading.Thread(target=drawing)

    t1.start()
    t2.start()

    print(threading.enumerate())


if __name__ == '__main__':
    main()