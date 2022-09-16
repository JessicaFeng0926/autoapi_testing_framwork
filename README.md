# autoapi_testing_framwork
## 简易API自动化测试框架
一款数据驱动、只需双击批处理文件就能执行全部测试用例并生成测试报告的API自动化测试框架。
### 技术栈
python<br/>
pytest<br/>
requests<br/>
logging<br/>
yaml<br/>
xlrd<br/>
allure<br/>
### 目录结构
│  load_data.py<br/>
│  pytest.ini<br/>
│  README.md<br/>
│  requirements.txt<br/>
│  simple_logger.py<br/>
│  simple_requests.py<br/>
│  start.bat<br/>
│  test_cases.py<br/>
├─data<br/>
│&nbsp;&nbsp;&nbsp;&nbsp;data.xlsx<br/>
│&nbsp;&nbsp;&nbsp;&nbsp;data.yaml<br/>
├─logs<br/>
├─reports<br/>
├─temps<br/>
### 使用方法
1. 写入测试用例数据。可以在.xlsx和.yaml两种文件格式中选取比较熟悉的一种，比如更熟悉.xlsx文件格式，那就到data文件夹下，把data.yaml文件的内容清空。然后修改data.xlsx文件中的内容，把数据替换成要执行的测试用例数据。
2. 双击start.bat文件执行测试用例并生成测试报告。
3. 如果自动启动的ie浏览器无法显示测试报告的内容，可以把地址栏的地址复制粘贴到谷歌浏览器中查看测试报告。
### 各目录及文件介绍
***load_data.py:*** 加载存放在data.xlxs和data.yaml中的测试用例数据，并以类似列表的数据格式返回。<br/>
***pytest.ini:*** 对pytest的配置。包括指定了allure生成的数据的存放位置等。<br/>
***README.MD:*** 项目介绍，即此时此刻各位看到的文字。<br/>
***requirements.txt:*** 本项目依赖的python第三方库列表。将本项目下载到本地后，建议先在命令行执行`python -m pip install -r requirements.txt`完成对第三方库的安装。<br/>
***simple_logger.py:*** 创建并配置了用于整个项目使用的日志记录器。<br/>
***simple_requests.py:*** 对发送http请求的代码进行了封装。可以处理各种类型的http请求。并且本项目中的所有http请求都被封装到一个会话里。<br/>
***start.bat:*** 把启动测试、生成allure报告和渲染并打开allure报告的命令写入了这个批处理文件，只要双击该文件就可以方便地按步骤执行，省下了每次在命令行输入指令的时间。<br/>
***test_cases.py:*** 这是pytest可以执行的测试用例，使用了参数化测试用例的技术，可以把我们存入data.xlsx和data.yaml中的测试用例全部执行。<br/>
***data目录*** 存放测试用例数据，这也是我们主要操作的目录，体现了整个框架数据驱动的特性。<br/>
***logs目录*** 存放以日期为单位的日志文件。<br/>
***reports目录*** 存放allure生成的测试报告。<br/>
***temps目录*** 存放用于生成测试报告的数据。<br/>











