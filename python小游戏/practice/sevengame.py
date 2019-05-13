money = 10
# if not (money < 100):
# if money >= 100:

name = '小甲鱼'
'鱼'in name   # Ture
'肥鱼'in name  # Flase

x=1
y=2
z=3
x,y,z = z,y,x

# 按照 100 分制，90 分以上成绩为 A，80 到 90 为 B，60 到 80 为 C，60 以下为 D，
# 写一个程序，当用户输入分数，自动转换为ABCD 的形式打印。
score = input('请输入一个分数：')
if 80 > score >= 60:
    print('C')
elif 90 > score >= 80:
    print('B')
elif 60 > score >= 0:
    print('D')
elif 100 >= score >= 90:
    print('A')
else:
    print('输入错误！')

# 请将以下代码修改为三元操作符实现：
x,y,z = 6,5,4
if x<y:
    small = x
    if z < small:
        small = z
elif y < z:
    small = y
else:
    small =z

small = x if (x < y and x < z) else (y if y < z else z)

# 条件表达式
x,y = 4,5
if x<y:
    small = x
else:
    small = y

small = x if x < y else y


# 断言（assert）
# assert这个关键字我们称之为“断言”，当这个关键字后边的条件为假时
# 程序自动崩溃并抛出AssertionError的异常。当这个关键字后边的条件为真时，程序无影响。


