import re 
import requests 
from simple_logger import LOGGER
import time 

class RequestsHandler:
    def __init__(self):
        self.headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
            }

    def get_response(self,method,url,params):
        '''
        完成请求并返回响应 如果无法识别请求类型 会返回包含错误信息的响应
        '''
        time.sleep(0.5)
        if method == 'GET':
            LOGGER.info("正在处理GET请求")
            return requests.get(url=url,params=params,headers=self.headers)
        elif method == 'POST':
            LOGGER.info("正在处理POST请求")
            return requests.post(url=url,data=params,headers=self.headers)
        else:
            res = requests.Response()
            res.status_code = 400
            LOGGER.error("无法识别请求类型")
            return res

    def check_response(self,response,code,pattern):
        '''
        检查请求的范围值是否符合预期

        response: 调用get_response方法得到的返回值
        return: 如果符合预期就返回True，否则返回False
        '''
        flag = True
        if response.status_code != code:
            LOGGER.info(f"返回状态码不符{response.status_code}!={code}")
            flag = False
        com = re.compile(pattern)
        if not com.findall(response.text):
            LOGGER.info(f"不存在指定的字符串模式[{pattern}]")
            flag = False 
        return flag


if __name__ == '__main__':
    from load_data import Data 
    data = Data()
    number, name, url, method, params, code, pattern = data[1]
    rh = RequestsHandler()
    response = rh.get_response(method,url,params)
    print(response.text)
    print(rh.check_response(response,code,pattern))
    

        


