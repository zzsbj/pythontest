#1.	把字符串转成列表 - list()
# str1 = "python"
# def list_str():
#     list1 = list(str1)
#     #print(list1)
#     return list1
# result = list_str()
# print(result)
#2.	完成任意整数序列的相加 - 生成一个整数序列，里面全是数字。求里面所有数字的和
def add_fun(num):
    sum = 0
    for i in range(num):
        sum+=i
    print(sum)
add_fun(100)
# #3.	定义函数：判断一个对象（列表，字典，字符串）的长度是否大于5，如果大于5，输出True；否则输出False。---if 判断嵌套
def fun_len(obj):
    if type(obj) == dict or type(obj) == list or type(obj) == str:
    #if isinstance(obj,dict) or isinstance(obj,list) or isinstance(obj,str)
        if len(obj) >= 5 :
            print("True")
        else :
            print("Flase")
    else:
        print("数据类型不能计算长度！")  #容错性友好
fun_len("1234")



