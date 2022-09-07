import logging 
from datetime import datetime 
import os 

__all__ = ['LOGGER']

# 创建一个记录器
LOGGER = logging.getLogger()
LOGGER.setLevel(logging.DEBUG)

# 创建一个控制台处理器
console_handler = logging.StreamHandler()
# 创建一个文件处理器
time = datetime.now()
stamp = time.strftime("%Y%m%d")
logsdir = os.path.join(os.path.dirname(__file__),'logs')
filepath = os.path.join(logsdir,f'log{stamp}.log')
file_handler = logging.FileHandler(filepath,mode='a')

# 创建一个格式
formatter = logging.Formatter('%(levelname)8s | %(filename)s | Line%(lineno)s | %(asctime)s | %(message)s')

# 把格式应用于两个处理器
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# 把处理器装载到记录器里
LOGGER.addHandler(console_handler)
LOGGER.addHandler(file_handler)
