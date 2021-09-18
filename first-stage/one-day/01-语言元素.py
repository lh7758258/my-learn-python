"""
@Time       : 2021-09-18 22:41:42
@Author     : Mr.szf
@description: 
"""

print("hello, python")

a = 10
b = 20
print(float(a))
print(str(b))
c = str(b)
print(type(c))

# 练习
# 1.华氏温度转换为摄氏温度。
d = float(input('请输入华氏温度：'))
e = (d - 32) / 1.8
print()
print('%.1f 华氏度 = %.1f摄氏度' % (d,e))

# 2.输入圆的的半径计算周长和面积
h = int(input("亲属人圆的半径："))
s = 3.14 * h * 2
area = 3.14 * h * h
print("半径为 %d 的圆的周长为 %.1f,面积为 %.1f" % (h, s, area))

# 3.输入年份判断是不是闰年。
year = int(input("请输入年份："))
if year % 4 == 0 and year % 100 != 0 or  year % 400 == 0:
    print('%d是闰年' % year)
print('%d不是闰年' % year)