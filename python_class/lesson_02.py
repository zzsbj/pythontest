'''
字符串的操作
1、取值：元素 位置---索引，从0开始，依次＋1
2、取多个值：切片  [开始：结束：步长]  ---取头不取尾
开始头   省略，默认从0开始
结束   省略，默认末尾结束
步长  省略，默认是1
3、负数 从右边开始取，最后一个是-1
4、元素个数  len()---内置函数：统计元素个数（长度）
5、替换字符串里的元素  replace()
6、index  find
'''
info = ('python自动化课程')
str1 = 'hello world!'     #12个元素
print(len(str1))
print(str1[1])            # e
print(str1[2:5:1])        # llo
print(str1[:5:1])         #hello
print(str1[2::2])         #lowrd
print(str1[::])           #hello world!
print(str1[-1])           #！
print(str1[2:len(str1):4])   #lwd

str1 = str1.replace("world","tricy")
print(str1)      # hello tricy!
print(str1.index("h"))   #0
print(str1.find("h"))    #0
#print(str1.index("x"))  #如果元素没有找到，会报错，代码终止运行
print(str1.find("x"))   #单独运行，结果是-1   如果元素没有找到，不报错，不终止运行
print(str1.count("h"))
'''
格式化输出
第一种 .format()
1、占位符 {}--传变量的地方  .format()
2、 .format() 可以默认按顺序传入变量  也可以指定位置传   ---不能混合使用
（了解）第二种 %   %s---字符串,匹配所有   %d---整数   %f---小数

'''
name = "tim"
age = 18
hobby = "吃"
print('''---{2}---
name:{2}
age:{0}
hobby:{1}
'''.format(age,hobby,name)
)

'''
python运算符
1、算数运算符  + - * /
print(10 +20)    #两个数字相加
print("love" + "tricy")    #两个字符串拼接
print(srt(123) + "abc")    
# str()：强制字符串转化    int()   float()  bool()
print(30 - 20)   #两个数字相减
print(2 * 3）   #两个数字相乘
print（“I love you" * 3000)   #字符串重复输出*次
print(10 / 2)   # 5.0  结果是浮点型
2、赋值运算符 =  +=  -=
3、比较运算符 < <=  > >=  == !=
print("登陆成功"="登陆成功")   #判断字符串是否相等  执行结果-预期结果
4、逻辑运算符 and  or not
print(not 2 > 3)         #True
5、成员运算符  in   not in
str2 = "python"
print("p" in str2)       #True
'''
num = input("请输入你的数字")  #input() 内置函数  在控制台输入数据，赋值给num变量
print(num)