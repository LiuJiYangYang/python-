# 下面的循环会打印多少次"I Love FishC"？
for i in range(0,10,2):
    print('I Love FishC')
# 5次

# 下面的循环会打印多少次"I Love FishC"？

'''
for i in 5:
    print('I Love FishC')
'''
# 会报错，上节课的课后习题我们提到了 in 是“成员资格运算符”，而不是像 C 语言那样去使用 for 语法。
# Python 的 for 更像脚本语言的 foreach。

while True:
    while True:
        break
        print(1)
    print(2)
    break
print(3)     # 打印出：2     3

# 提供该while效率
i = 0
string = 'ILoveFishC.com'
while i < len(string):
    print(i)


i = 0
string = 'ILoveFishC.com'
length = len(string)
while i < length:
    print(i)
    i += 1

count = 3
password = 'FishC.com'

while count:
    password = input('请输入密码：')
    if password == password:
        print('密码正确，进入程序......')
        break
    elif '*' in password:
        print('密码中不能含有“*”号！你还有',count,'次机会',end='')
        continue
    else:
        print('密码输入错误！你还有',count-1,'次机会！',end='')
    count -= 1


# 如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数
# 153 = 1^3 + 5^3 + 3^3，因此 153 就是一个水仙花数
for i in range(100, 1000):
    sum = 0
    temp = i
    while temp:
        sum = sum + (temp%10) ** 3
        temp //= 10
    if sum == i:
        print(i)


# 三色求问题
print('red\tyellow\tgreen')
for red in range(0,4):
    for yellow in range(0,4):
        for green in range(2,7):
            if red + yellow + green == 8:
                print(red, '\t', yellow, '\t',green)
                # 不是字符串拼接，不能用“+”

