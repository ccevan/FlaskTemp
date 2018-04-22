# Author: c.evan
# -*- coding: utf-8 -*-

# 使用方式
'''
在需要使用的模块中导入该模块
from loggings import logger
直接logger.error(e)就可以了

'''

import logging

# create logger
# logger_name = __name__
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
# 终端输出的级别

# create file handler
log_path = "./log.log"  #文件存放位置
fh = logging.FileHandler(log_path)
fh.setLevel(logging.WARN)
# 日志级别

# create formatter
fmt = "%(asctime)-15s %(levelname)s %(filename)s %(lineno)d %(process)d %(message)s"
# datefmt = "%a %d %b %Y %H:%M:%S"
datefmt = "%Y-%m-%dT%H:%M:%S"

formatter = logging.Formatter(fmt, datefmt)

# add handler and formatter to logger
fh.setFormatter(formatter)
logger.addHandler(fh)






