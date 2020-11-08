'''
常用数据类型（续） 列表（list） 元组  字典  集合
列表（list）： []
1、元素可以是任意数据类型  int  float bool  str  list tuple
2、取值：索引取值---类比字符串
取多个值：切片
扩展：列表的嵌套取值
3、列表的元素是可以被改变的！---增加、修改、删除
4、列表元素可以重复   统计个数:count
5、len()   统计元素个数
'''
list1 = [20,3.14,True,"七木","荷花鱼",[1,2,3,4]]
print(list1[1])      # 3.14
print(list1[3:5])    # ['七木', '荷花鱼']
print(list1[5][1])   # 2
#增加
list1.append("焕蓝")     # 默认追加元素到列表的末尾 [20, 3.14, True, '七木', '荷花鱼', [1, 2, 3, 4], '焕蓝']
list1.insert(5,"kingo")   # 指定位置进行元素插入 [20, 3.14, True, '七木', '荷花鱼', 'kingo', [1, 2, 3, 4], '焕蓝']
list1.extend(["十又","寸草","小丑"])    # 两个列表合并 [20, 3.14, True, '七木', '荷花鱼', 'kingo', [1, 2, 3, 4], '焕蓝', '十又', '寸草', '小丑']
#删除
list1.pop()  # 默认删除最后一个元素 [20, 3.14, True, '七木', '荷花鱼', 'kingo', [1, 2, 3, 4], '焕蓝', '十又', '寸草']
list1.pop(0)     #可以指定位置（索引）进行删除
list1.remove(3.14)      # 指定元素本身进行删除  [True, '七木', '荷花鱼', 'kingo', [1, 2, 3, 4], '焕蓝', '十又', '寸草']
#list1.clear()  # 清楚所有元素  空列表
print(list1)
# 修改  ---取值 重新赋值
list1[4] = "amiee"   #替换
list1.append("kingo")
print(list1)
print(list1.count("kingo"))
'''
元组
1、元素可以是任意数据类型  int  float bool  str  list tuple
2、取值：索引取值---类比字符串
取多个值：切片
扩展：列表的嵌套取值
3、元组的元素不可以被改变！
4、元组元素可以重复   统计个数:count
5、len()   统计元素个数
6、list tuple ---扩展：数据类型转换
'''
tuple1 = (20,3.14,True,"七木","荷花鱼",[1,2,3,4])
print(tuple1)    # (20, 3.14, True, '七木', '荷花鱼', [1, 2, 3, 4])
print(tuple1.count(20))
#转换
list1 = list(tuple1)
list1[2] = "小丑"
tuple2 = tuple(list1)
print(tuple2)  # (20, 3.14, '小丑', '七木', '荷花鱼', [1, 2, 3, 4])
'''
字典：dictionary {}
1、元素：key:value （键值对）
2、场景：存储数据属性： 人---名字、身高、体重
key:1)一般字符串，不能是可以改变的数据类型（list、dict)
    2)不能重复，唯一
value:可以是任意数据类型  可被改变---增删改
3、字典没有顺序 不能索引取值，通过key取value
'''
dict1 = {"name":"tan","height":"173","weight":"160"}
print(dict1["height"])   #通过key---value         1
print(dict1.get("weight"))  # 通过key---value     2
# 修改
dict1["weight"] = "150"    # 修改对应key的value
print(dict1)   #{'name': 'tan', 'height': '173', 'weight': '150'}
# 增加
dict1["age"] = 18  # key不存在，新增加键值对
print(dict1)   #{'name': 'tan', 'height': '173', 'weight': '150', 'age': 18}
dict1.update({"city":"北京","hobby":"学习python","gender":"boy"})   #字典的合并
print(dict1)
# 删除
dict1.pop("weight") # 指定key删除 删除对应键值对
print(dict1)  #{'name': 'tan', 'height': '173', 'age': 18}
del dict1   #变量存储删除 对象不存在了
'''
集合: set  {} 元素单个
1、无序
2、元素不可以重复  --- 使用场景：去重
'''
list2 = [11,22,22,33,33,44]
set1 = set(list2)    #list--->set
print(set1)     #{33, 11, 44, 22}
list3 = list(set1)   # set--->list
print(list3)
'''
控制流： 代码执行顺序 ---从上至下依次执行  判断  循环
判断：if 语法
if 条件 ：    冒号：缩进 父子关系
    子代码（执行语句）
elif 条件：
    子代码（执行语句）
    ...（elif可以没有 可以多个）
else ： (可以没有）
    执行语句
'''
money = int(input("请输入你的余额：")) #input() 控制台输入，类型默认：字符串
if money > 500:
    print("买房")
elif money > 200:
    print("买车")
elif money > 50:
    print("存着")
else:
    print("滚去学习")
dict()
dict1 = {"name":"tricy","age":18}
dict2 = dict(name = "tricy",age = 18)
print(dict1)
print(dict2)  #结果一样