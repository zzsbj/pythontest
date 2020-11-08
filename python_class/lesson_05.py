'''
web自动化：
代码           翻译（中间人）        浏览器
Python ---->   浏览器驱动 ---->      Chrome
selenium:是Python的一个工具，有三部分
1）ide :录制脚本---用的少
2）webdriver:库 ---提供对网页的各种操作+ Python Java  只导入这部分
3）grid :分布式---少
'''
from selenium import webdriver  #从selenium工具里导入webdriver库
import time  #导入time这个模块  ---Python自带的
driver = webdriver.Chrome()  #选择Chrome浏览器，初始化  ==可以与浏览器进行沟通，建立会话session
driver.implicitly_wait(10)  #隐式等待，默认等待10s ---> 最多等到10s,提前出现了，不在继续等待
#1、打开一个网址
driver.get("http://erp.lemfix.com")
#2、浏览器窗口最大化
driver.maximize_window()
# #3、打开新的页面
# time.sleep(3)  #等待 默认秒
# driver.get("http://120.78.128.25:8765")
# #4、前进 后退 刷新
# time.sleep(3)
# driver.back()  #退回上一个页面
# time.sleep(3)
# driver.forward()#前进到下一个页面
# time.sleep(3)
# driver.refresh()#刷新页面
# #5、退出
# driver.quit() #关闭驱动 session关闭
# driver.close() #关闭当前窗口，不退出会话

#以上是浏览器的常规操作   非常规操作，怎么实现---元素定位  了解前端页面

'''
基础知识：web页面 = HTML + CSS + JavaScript
HTML:标签语言 <标签名> 值 </标签名>
css:页面布局设置，字体颜色，字体大小样式
JS:依据不同效果
  
元素的特征 ：根据页面设计规则 有些特征是惟一的  ===开发遵循了这个规则
id 类比身份证号 ===仅限于当前页面  username  password
注意：如果id不是固定的话，就不能用来定位

xpath :
1、绝对路径:/html/body/div/div/div[1]/a/b ---根节点，顺序性、
继承关系--失效     #  面试不说．工作里不用;
2、相对路径:只靠自己的特征定位  //开头--加上我关心节点


xpath元素定位
1、绝对路径/相对路径
标签名+属性=//标签名[@属性名=属性值]
//input[@id= "username"]    --xpath表达方式
2、层级定位:
//标签名[@属性名=属性值]//标签名[@属性名 = 属性值]                                                                                                                                                                      属性名=属性值]
//div[@class= "login-logo"]//b
3、文本属性定位: //b[text()="柠檬ERP"]
4、包含属性值://标签名[contains(@属性名/text(),属性值)]
---//input[contains(@class,"username")]

对页面进行对应的操作：
1、点击：click
2、传值：send_keys
3、获取页面文本：text
4、获取属性 attribute

但凡是切换了页面，页面没有加载完，元素不显示===最好加个等待;
三种等待方式：
1、强制等待： time.sleep(5)   必须完成了等待时间才往下执行
2、智能等待： driver.implicitly_wait(10)
隐式等待:可以设置等待时间，再这个等待时间还没有结束之前元素找到了，不继续等待，继续执行下面的代码:--灵活
注意:一个session里只执行一次。
显式等待: expected_condition == Python班级

八大元素定位方式
三大等待
四大操作
'''
driver.find_element_by_id("username").send_keys("test123") # 找到了有username这个id的元素，点击，输入内容
driver.find_element_by_id("password").send_keys("123456")  # 找到了有password这个id的元素，点击，输入内容
driver.find_element_by_id("btnSubmit").click()  # 找到了有btnSubmit这个id的元素，点击

#driver.find_element_by_xpath("//input[@id = 'username']").send_keys("test123")
page_text = driver.find_element_by_xpath('//div[@class = "login-logo"]//b').text  #找到这个元素的位置之后 获取文本  赋值给变量
page_title = driver.title # 获取页面的标题
print("这个页面的标题是：{}".format(page_title))
print(page_text)
if page_text =="柠檬ERP":
    print ("这个页面的标题是：{}".format(page_text))
else:
    print ( "这个条件测试用例不通过! ")
login_user = driver.find_element_by_xpath("//p[text()='测试用户']").text  #获取到登录用户名
if login_user =="测试用户":
    print("这个登录的用户是:{}".format (login_user))
else:
    print ("这个条件测试用例不通过!")
#点击零售出库
driver.find_element_by_xpath("//span [text()='零售出库']").click()



#点击搜索
#driver.find_element_by_id ("searchNumber") .send_keys ("314")  不可用
'''
1、识别是否有子页面的方式:页面层级路径里出现iframe:就需要去切换iframe 才可以进行元素的定位。
2、怎么去切换:
1)找到这个iframe元素。切换

切换三种方式：
1、通过id来切换
2、通过元素定位(xpath)来切换iframe
3、iframe下标：从0开始 HTML-页面=0  第一个宝宝=1 第二个宝宝=2
'''
#id = driver.find_element_by_xpath("//iframe [@id='tabpanel-bafba10ab5-frame']")
#driver.switch_to.frame('tabpanel-bafba10ab5-frame')     行不通

#找到这个元素，获取id属性
#p_id=driver.find_element_by_xpath("//li[@class='active']").get_attribute("id")
p_id=driver.find_element_by_xpath("//div[text()='零售出库']/..").get_attribute("id")
f_id = p_id + "-frame"
print(f_id)
#1、通过id进行iframe切换
# driver.switch_to.frame(f_id)
# driver.find_element_by_id ("searchNumber") .send_keys ("314")
#2、通过元素定位(xpath)来切换iframe
# driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='{}']".format(f_id)))
# driver.find_element_by_id ("searchNumber") .send_keys ("314")
#3、通过iframe下标来切换
driver.switch_to.frame(1)
driver.find_element_by_id ("searchNumber") .send_keys ("429")
#点击搜索按钮
driver.find_element_by_id("searchBtn").click()
time.sleep(1)   #隐式等待不生效时， 加强制等待
#找到单据编号
num = driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-0']//td[@field='number']/div").text
if "429" in num:
    print("搜索结果是正确的")
else:
    print("用例测试不通过")

