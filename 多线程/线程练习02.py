# coding = UTF-8
import threading, time
def loop(x):
    print("%s start" % threading.current_thread().name)
    for i in range(x):
        time.sleep(1)
        print("%s:%d" % (threading.current_thread().name, i))
    print("%s stop" % threading.current_thread().name)


print("%s start" % threading.current_thread().name)
t1 = threading.Thread(target=loop, args=(6, ))
# setDaemon应该放在start之前
t1.setDaemon(True)
t1.start()
# t1.join()
print("%s stop" % threading.current_thread().name)