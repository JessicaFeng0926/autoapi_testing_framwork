import yaml
import xlrd
import os 
from simple_logger import LOGGER

class Data(list):
    '''
    把存放在文件里的数据加载进来
    存入一个继承自列表类的数据类型
    '''
    def __init__(self):
        super().__init__()
        # data文件夹的路径
        self.datadir = os.path.join(os.path.dirname(__file__),'data')
        # data文件夹里全部的数据文件名列表
        self.filenames = os.listdir(self.datadir)
        self.__load_yaml()
        self.__load_xlsx()

    def __load_yaml(self):
        '''
        把data.yaml里的数据加载进来
        '''
        # 如果有yaml类型的数据文件 就把这个文件里的数据装载到data列表里
        if 'data.yaml' in self.filenames:
            with open(os.path.join(self.datadir,'data.yaml'),'r',encoding='utf8') as f:
                data_list = yaml.load(f,yaml.Loader)
                for dic in data_list:
                    temp = []
                    for key in ('number', 'name', 'url', 'method','params','code','pattern'):
                        temp.append(dic[key])
                    self.append(temp)
            LOGGER.info("加载了data.yaml中的数据")

    def __load_xlsx(self):
        '''
        把data.xlsx里的数据加载进来
        '''
        # 如果有xlsx类型的数据文件 就把这个文件里的数据也装载到data列表里
        if 'data.xlsx' in self.filenames:
            book = xlrd.open_workbook(os.path.join(self.datadir,'data.xlsx'))
            sh = book.sheet_by_index(0)
            for i in range(1,sh.nrows):
                row = sh.row(i)
                row = [cell.value for cell in row]
                self.append(row)
                # excel里的数字被加载进来之后默认是float类型
                # 需要手动转化为int类型
                self[-1][0] = int(self[-1][0])
                self[-1][5] = int(self[-1][5])
                # 把excel表格里的键值对从字符串转化为字典类型
                dict_str = self[-1][4]
                temp_dict = {}
                # 不为空字符串 我们才进行下一步处理 否则 不管
                if dict_str:
                    dict_list = dict_str.split(',')
                    for item in dict_list:
                        k,v = item.split(':')
                        temp_dict[k] = v 
                # 当参数是空字符串的时候 存入一个空字典
                self[-1][4] = temp_dict
            LOGGER.info("加载了data.xlsx中的数据")



if __name__ == '__main__':
    data = Data()
    print(data)
                
