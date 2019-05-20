# 形参和实参
# 函数文档

def MyFirstFunction(name):
    '函数定义过程中的name是叫形参'
    #因为Ta只是一个形式，表示占据一个参数位置
    print('传递进来的' + name + '叫做实参，因为Ta是具体的参数值！')
    return name      # 没
print(MyFirstFunction('鱿鱼'))


print(MyFirstFunction.__doc__)

# help(MyFirstFunction)
# 每个对象都会有一个__doc__属性，用于描述该对象的作用
print(print.__doc__)

# 关键字参数，参数名和参数值
def SaySome(name, words):
    print(name + '->' + words)

print(SaySome('小甲鱼','让编程改变世界！'))

print(SaySome('让编程改变世界！','小甲鱼'))
# 关键字参数
print(SaySome(words='让编程改变世界', name='小甲鱼'))

# 默认参数,未定义调用初值
def SaySome(name='小甲鱼',words='让编程改变世界！'):
    print(name + '->' + words)

print(SaySome('嘻哈'))

print('嘻哈', '笑看人生才是最美的生活')

# 可变参数,可添加多个值
def test(*params):
    print('参数的长度是：', len(params));
    print('第二个参数是：',params[1]);

print(test(1, '小甲鱼', 3.14, 5, 6, 7, 8))

def test(*params, exp):
    print('参数的长度是：', len(params));
    print('第二个参数是：',params[1]);

print(test(1, '小甲鱼', 3.14, 5, 6, 7, 8, exp=8))

# 给他一个默认参数
def test(*params, exp=8):
    print('参数的长度是：', len(params));
    print('第二个参数是：',params[1]);














