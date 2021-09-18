"""
@Time       : 2021-09-18 21:36:07
@Author     : Mr.szf
@description: 
"""

# 这是我第一行 python 代码
print("hello,world!")

# python基本数据类型
# 1.整型(int)       例：int a = 10;
# 2.浮点型(float)   例: float b = 3.455;
# 3.字符串型(str)   例：str c = 'wo';
# 4.布尔型(bool) 只有True和False两种   例：bool test = False;


"""
# 1.语言元素
z = 20
y = 2
print("*" * 20)
# 22
print(z + y)
# 18
print(z - y)
# 40
print(z * y)
# 10.0
print(z / y)
print("*" * 20)
a = 10
b = 1.28
c = "test one"
d = False
# type() 判断参数类型
# <class 'int'>
print(type(a))
# <class 'float'>
print(type(b))
# <class 'str'>
print(type(c))
# <class 'bool'>
print(type(d))
# 转成float类型  10.8
print(float(a))
# True
print(bool(a))
# True
print(bool(b))
# True
print(bool(c))
# False
print(bool(d))
print("=" * 20)
"""

"""
e = int(input("e = "))
f = int(input("f = "))
# 输入完 e 和 f 以下内容会自动计算
print(e + f)
"""


# 2.分支结构(if else)
# 需求： 用户身份验证  用户名 =  admin ， 密码 = 123456
username = input("请输入用户名：")
password = input("请输入密  码：")
if username == "zhangsan" and password == "123456":
    print("登录成功")
else:
    print("登录失败")