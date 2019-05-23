# 使用lambda表达式将下边函数转变为匿名函数
def fun_A(x, y=3):
    return x*y

lambda x,y=3:x*y


# 匿名函数转变为普通的函数
lambda x : x if x % 2 else None

def is_odd(x):
    if x % 2:
        return x
    else:
        return None

print(is_odd(5))

# 利用filter()和lambda表达式快速求出100以内所有3的倍数吗？
list(filter(lambda n : not(n%3), range(1,100)))

# 列表推导式代替filter()和lambda组合，
[i for i in range(1, 100) if not(i%3)]


# zip会将两数以元祖的形式绑定在一块
list(zip([1,3,5,7,9],[2,4,6,8,10]))

# 采用map和lambda表达式
list(map(lambda x, y : [x, y], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))
# 注意：强大的map()后边是可以接受多个序列作为参数的


def make_repeat(n):
    return lambda s:s*n

double = make_repeat(2)
print(double(8))
print(double('FishC'))


# Python允许使用lambda表达式创建匿名函数
def ds(x):
    return 2*x + 1
print(ds(5))
print(lambda x:2*x+1)

# Python的lambda语句是非常精简的，基本的语法就是在冒号的前面是原函数的参数，
# 而在冒号的后边是原函数的返回值
# ambda语句实际上是构建了一个函数对象，如果要对它进行使用，只需要简单的赋值即可
g=lambda x:2*x+1
print(g(5))


# lambda语句构建的函数的参数也可以是多个的
# add(2,3)
a=lambda x,y:x+y
print(a(2,3))


print(filter(None,[1,0,False,True]))

print(list(filter(None,[1,0,False,True])))

# filter()选出奇数的代码
def odd(x):
    return x%2
show=filter(odd,range(10))
print(list(show))

# 用lambda实现
print(list(filter(lambda x:x%2, range(10))))

# map()     map(func, *iterables)
print(list(map(lambda x:x*2,range(10))))


















