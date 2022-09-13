import pytest 
from load_data import Data 
from simple_logger import LOGGER
from simple_requests import RequestsHandler
import requests 

@pytest.mark.parametrize(
        [
        'number',
        'name',
        'url',
        'method',
        'params',
        'code',
        'pattern',
        ],
        Data())
def test_api(number,name,url,method,params,code,pattern):
    '''接口测试函数'''
    LOGGER.info(f'测试用例【#{number} {name}】开始执行')
    rh = RequestsHandler()
    headers = {
        'User-Agent': 
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    }
    response = requests.Response()
    if method.lower() == 'get':
        response = rh.get_response(method,url,headers=headers,params=params)
    elif method.lower() == 'post':
        response = rh.get_response(method,url,headers=headers,data=params)
    assert rh.check_response(response,code,pattern) == True 
    LOGGER.info(f'测试用例【#{number} {name}】执行完毕')



