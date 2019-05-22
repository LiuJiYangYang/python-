# 分辨下面函数的形参和实参
def MyFun(x):
    return x**3

y=3
print(MyFun(y))
# x是形参，y是实参


# 计算打印所有参数的和乘以基数（base=3）的结果
# 如果参数中最后一个参数为(base=5)，则设定基数为5，基数不参与求和计算。
def sum_x_base(*numbers, base=3):
    sum=0
    for number in numbers:
        sum+=numbers
    if numbers[-1]==5:
        base=5
        return sum
    else:
        return sum*base


def mFun(*param, base=3):
    result = 0
    for each in param:
        result += each

    result += base

    print('结果是：', result)

mFun(1, 2, 3, 4, 5, base=5)

# 如果一个3位数等于其各位数字的立方和，则称这个数为水仙花数，例如153=1^3+5^3+3^3,
# 因此153是一个水仙花数，编写一个程序，找出所有的水仙花数。

def shuixianhuaFun(num):
    sum = 0
    cnt = 0
    temp = num
    while cnt < 3:
        cnt += 1
        sum += (num % 10) ** 3
        num //= 10
    if sum == temp:
        return sum

for i in range(100, 1000):
    shuixianhuaFun(i)

def Narcissus():
    for each in range(100, 1000):
        temp = each
        sum = 0
        while temp:
            sum = sum + (temp%10)**3
            temp = temp//10  # 注意这里用地板除

        if sum == each:
            print(each, end='\t')
print('所有的水仙花分别是：', end='')
Narcissus()


# 编写findstr()函数，字符串im出现的次数
def findstr(substr, objectstr):
    print('子字符串在目标字符串中共出现'+str(objectstr.count(substr)+'次'))

def findstr(desStr, subStr):
    count = 0
    length = len(desStr)
    if subStr not in desStr:
        print('在目标字符串中未找到字符串')
    else:
        for each1 in range(length-1):
            if desStr[each1] == subStr[0]:
                if desStr[each1+1] == subStr[1]:
                    count +=1
        print('字符串在目标字符串中共出现%d次' %count)
desStr = input('请输入目标字符串：')
subStr = input('请输入字符串（两个字符）：')
findstr(desStr, subStr)





































