# coding = UTF-8
import threading, time
exitFlag = 0


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            exit(1)
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.threadLock = threading.Lock()

    def run(self):
        print("Strating " + self.name)
        self.threadLock.acquire()
        print_time(self.name, self.counter, 5)
        self.threadLock.release()
        print("Exiting " + self.name)

t1 = myThread(1, "Thread-1", 1)
t2 = myThread(2, "Thread-2", 2)

t1.start()
t2.start()
t1.join()
t2.join()

print("Exiting Main Thread")