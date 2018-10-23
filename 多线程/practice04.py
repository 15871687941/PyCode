from multiprocessing import Process, Queue, cpu_count
import os, time, random


def write(queue):
    print("Process to write:%s" % os.getpid())
    for value in "ABCDEFGHIJKLMNOPQRSYUVWXYZ":
        print("Put %s to queue..." % value)
        queue.put(value)
        time.sleep(random.random())


def read(queue):
    print("Process to read:%s" % os.getpid())
    while True:
        value = queue.get()
        print("Get %s from queue." % value)


if __name__ == '__main__':

    queue = Queue()
    print(cpu_count(), type(queue))
    pr = Process(target=read, args=(queue, ))
    pw = Process(target=write, args=(queue, ))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()