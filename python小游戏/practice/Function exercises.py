
# 定义函数是错误的,函数传递的是变量，不是数据类型的实体，具体见后面答案
# def MyFun((x,y)(a,b)):

# def MyFun(x, y):        # 报错，int类型的变量不可阅读
#     return x[0]*x[1]-y[0]*y[1]
# print(MyFun(3,4),(1,2))

def hello():
    print('hello World!')
    return
    print('Welcome To FishC.com!')

print(hello())
# 当Python执行到return语句的时候，Python认为函数到此结束
# 打印 Hello World！


# 编写一个函数power()模拟内建函数pow()，即power(x, y)为计算并返回x的y次幂的值。
# pov(x,y)=x**y
def power(x, y):
    return x**y

'''
# 需进一步思考下
def power(x,y):
    result = 1
    for i in range(y):
        result*=x
    return result
print(power(2,3))
'''

# 利用欧几里得算法（脑补链接）求最大公约数
def gcd(x, y):
    for each in range(1,x+1):
        if (x%each == 0 and y%each == 0):
            max = each
    return max
'''
def gcd(x,y):
    while y:
        t = x%y
        x=y
        y=t
        
    return x
print(gcd(4,6))
'''

# 将十进制转换为二进制的函数，要求采用“除2取余”（脑补链接）的方式
def ten2two(x):
    result = ''
    list1 = list()
    while (x//2!=0):
        list1.append(x%2)
        x//=2
    else:
        list1.append(x%2)
    while list1:
        result+=str(list1.pop())
    return result

'''
def Dec2Bin(dec):
    temp = []
    result = ''

    while dec:
        quo = dec % 2
        dec = dec // 2
        temp.append(quo)
    while temp:
        result += str(temp.pop())
    return result

print(Dec2Bin(62))
'''
def Dec2Bin(dec):
    temp = []
    result = ''

    while dec:
        quo = dec % 2
        dec = dec // 2
        temp.append(quo)

    while temp:
        result += str(temp.pop())
    return result
print(Dec2Bin(62))






