# 递归
def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

number = int(input('请输入一个正整数：'))
result = factorial(number)
print('%d 的阶乘是 ： %d' %(number, result))

# 斐波那契       数列
# 后面的数是前面两个数的和

'''
      1,当n=1
F(n)= 2,当n=2
      F(n-1)+F(n-2),当n>2
'''
# 迭代算法，速度快
def fab(n):
    n1=1
    n2=1
    n3=1
    if n<1:
        print("请输入错误！")
        return -1
    while (n-1)>0:
        n3=n2+n1
        n1=n2
        n-=1
    return n3

result = fab(20)
if result != -1:
    print("总共有%d对小兔崽子诞生！" % result)



# 递归算法，效率
def fab(n):
    if n<1:
        print("输入有误！")
        return -1
    if n==1 or n==2:
        return 1
    else:
        return fab(n-1)+fab(n-2)

result = fab(20)
if result != -1:
    print("总共有%d对小兔崽子诞生！" % result)
# 分制思想














































