import logging

logging.basicConfig(filename="example.log", level=logging.INFO)  # 日志写入文件
logging.basicConfig(format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
logging.warning("user [alex] attempted wrong password more than 3 times")
logging.critical("server is down")