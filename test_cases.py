import pytest 
from load_data import Data 
from simple_logger import LOGGER
from simple_requests import RequestsHandler

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
    response = rh.get_response(method,url,params)
    assert rh.check_response(response,code,pattern) == True 
    LOGGER.info(f'测试用例【#{number} {name}】执行完毕')



