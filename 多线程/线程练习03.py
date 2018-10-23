# coding = UTF-8
import threading

deposit = 0
lock_deposit = threading.Lock()

def change_it(n):
    global deposit
    deposit = deposit + n
    deposit = deposit - n

def loop(n):
    for i in range(100000):
        lock_deposit.acquire()
        try:
            change_it(n)
        finally:
            lock_deposit.release()

t1 = threading.Thread(target=loop, args=(5, ))
t2 = threading.Thread(target=loop, args=(8, ))
t1.start()
t2.start()
t2.join()
t2.join()
print(deposit)