import re 
import requests 
from simple_logger import LOGGER
import time 

class RequestsHandler:
    session = requests.Session()

    def get_response(self,method,url,**kwargs):
        '''
        完成请求并返回响应 如果出现异常 会返回包含错误信息的响应
        '''
        time.sleep(0.5)
        res = requests.Response() 
        try:
            res = self.__class__.session.request(method,url,**kwargs)
        except Exception as e:
            LOGGER.exception(e)
        finally:
            LOGGER.info(f"正确处理了{method}请求")
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
    

        


