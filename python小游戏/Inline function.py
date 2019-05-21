# 关键字
# 全局变量和局部变量
count = 5
def MyFun():
    count = 10
    print(10)

print(MyFun())
print(count)

# 修改全局变量global
def MyFun():
    global count
    count = 10
    print(10)
print(MyFun())
print(count)

# 内置函数
def fun1():
    print('fun1()正在被调用....')
    def fun2():
        print('fun2()正在被调用.....')
    fun2()
print(fun1())
# print(fun2())  # 报错

# 闭包closure,    list语言
# 对在内部函数里的变量
def FunX(x):
    def FunY(y):
        return x*y
    return FunY

i=FunX(8)
print(i)

print(i(5))
print(FunX(8)(5))    # 不能调用

'''
def Fun1():
    x=5
    def Fun2():
        x *= x
        return x
    return Fun2()
print(Fun1())      # 赋值前引用的局部变量“x”
'''
# 容器
def Fun1():
    x=[5]
    def Fun2():
        x[0] *= x[0]
        return x[0]
    return Fun2()
print(Fun1())      # 赋值前引用的局部变量“x”


def Fun1():
    x=5
    def Fun2():
        nonlocal x     # 使用nonlocal，表示他不是
        x *= x
        return x
    return Fun2()
print(Fun1())