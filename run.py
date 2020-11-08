from python_class import lesson_07   #导入函数文件
from test_data import test_data  #导入测试数据文件
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)
# 调用函数   1.先参数取出来   2.传参到函数调用里
url = test_data.url["url"]
user = test_data.login_data["username"]
pwd = test_data.login_data["password"]
s_key = test_data.s_key["s_key"]
#给函数定义了一个返回值  调用时用一个变量接收返回值
result = lesson_07.search_key(driver=driver,url=url,username=user,password=pwd,s_key=s_key)

if s_key in result:
    print("搜索结果是正确的")
else:
    print("用例测试不通过")
