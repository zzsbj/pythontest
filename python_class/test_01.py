# name = input("请输入姓名")
# age = input("请输入年龄")
# sex = input("请输入性别")
# print("*" * 20)
# print('''姓名:{0}
# 性别:{1}
# 年龄:{2}'''.format(name,sex,age))
# print("*" * 20)

str1 = 'python hello aaa 123123aabb'
# 1
print(str1[0:6:1])
# 2
print("o a" in str1)
print("he" in str1)
print("ab" in str1)
# 3
print(str1.replace("python","lemon"))
# 4
print(str1.index("aaa"))