import random, time, queue
from multiprocessing.managers import BaseManager

# 发送任务队列
from multiprocessing import freeze_support

task_queue = queue.Queue()
# 接收结果队列
result_queue = queue.Queue()


# 继承BaseManager
class QueueManager(BaseManager):
    pass


def get_task_queue():
    global task_queue
    return task_queue


def get_result_queue():
    global result_queue
    return result_queue


if __name__ == '__main__':
    freeze_support()
    # 把两个Queue都注册到网络上
    QueueManager.register('get_task_queue', get_task_queue)
    QueueManager.register('get_result_queue', get_result_queue)
    # 绑定端口5000，设置验证码123456
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'123456')
    # 启动
    manager.start()
    # 通过网络访问Queue
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    # 放置任务
    for i in range(10):
        n = random.randint(0, 1000)
        print("Put task %d..." % n)
        task.put(n)
    print("Try get results...")
    # 读取任务
    for i in range(10):
        r = result.get(timeout=None)
        print("Result: %s" % r)
    # 关闭
    manager.shutdown()
    print("master exit.")

