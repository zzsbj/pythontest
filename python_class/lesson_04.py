'''

''''''
for 循环 ：遍历数据对象里的所有元素：str list tuple dict
语法：
for 变量名 in 数据对象 ：
    子代码(循环体）
循环多少次由什么决定   --- 元素个数
中断：break  contine
range()---内置函数 ：生成一个整数序列 1，2,3,4，5,6
跟for循环一起使用 start（默认是0）,stop,step（默认是1）  取头不取尾
'''
count = 0  #计数器
list1 = [True, '七木', '荷花鱼', 'kingo', [1, 2, 3, 4], '焕蓝', '十又', '寸草']
for name in list1:
    if name == "荷花鱼":
        #break  #跳出整个循环，循环结束
        continue   #跳出本次循环
    print(name)
    print("*" * 20)
    count += 1
print(count)
print(len(list1))
# 还可以遍历元组，字典，字符串等
for i  in range(3,7,1):
    print(i)
'''
函数：封装成函数，调用 === 提高代码的复用率，提高执行效率
语法：
def 函数名():
    子代码（函数体）  ---实现功能
注意：函数只定义了，没调用，不会执行   ---如何调用？ 写函数名

函数里不固定的数据---定义成函数的参数 括号里
1、形参 ：函数定义的时候 定义的
2、实参：调用函数传入参数

参数定义的类型：
1、必备参数：定义了就必须要传入的参数---不传会报错
2、默认参数（缺省参数）：可以定义时赋默认值，调用时不传入  可以传，替换默认值
注意：默认参数必须在必备参数后面
3、不定长参数:等前面的必备参数和默认参数都接受完了，剩下的参数都给不定长参数。
*args:接受不确定数值，个数的参数 ---可不传，可传>=1个，元组接收 传参方式---位置传参
**kargs:字典接收，传参方式---关键字传参方法
''''''
传参的方式类型：
1、位置传参:按照位置参数传入
2、关键字传参﹔指定参数名来进行传参，不关心顺序--可靠
3、混合传参:注意:关健字传参必须跟在位置传参后!
报错 SyntaxError: positional argument follows keyword argument
'''
def good_job(salary,bonus,subsidy=500,*args,**kwargs):  # 定义：函数的参数  形参---变量替代
    sum1 = salary + bonus + subsidy
    # print("salary的值：{}".format(salary))
    # print("bonus的值：{}".format(bonus))
    # print("subsidy的值：{}".format(subsidy))
    # print("args的值：{}".format(args))
    # print("kwargs的值：{}".format(kwargs))
    for i in args:
        sum1 += i
    for j in kwargs:  #  j是key
        # print(kwargs.get(j))   #通过key取value
        sum1 += kwargs.get(j)
    #print("这份工作的工资总和是：{}".format(sum1))
    return sum1  #定义一个返回值
result = good_job(8000,2000,800,100,200,300,aa=50,bb=100,cc=200,dd=300)
print(result)
if result > 10000:
    print("这是不错的工作")
else:
    print("我还可以找到更好的")
'''
有进有出:进---参数，出---返回值
返回值:函数可以给到外面的人用的数据，做后续操作---调用函数的时候，可以获取到这个返回值--return
1、定义
2、调用--变量接收返回值 
3、如果没有返回值-- 返回None，可以有return :可以有多个---元组保存
4、注意:返回值写在函数的最后–--标志着函数的结束
'''
'''
内置函数:
print ()
input() ---字符串
type ()
instance ()
len ()
replace ,count, find ,index,append,insert,pop,remove,update---数据类型的内置方法
str()  float()  int()  list()  tuple()  dict()  bool()  set()
range() --整数序列
'''
