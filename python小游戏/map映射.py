# 当索引不好用时
# 创建和访问字典
brand = ['李宁', '耐克', '阿迪达斯', '鱼C工作室']
slogan = ['一切皆有可能', 'Just do it', 'Impossible is nothing', '让编程改变世界']
print('鱼C工作室的口号是：',slogan[brand.index('鱼C工作室')])

dict1 = {'李宁': '一切皆有可能', '耐克': 'Just do it', '阿迪达斯':'Impossible is nothing', '鱼C工作室':'让编程改变世界'}
print('鱼C工作室的口号是：', dict1['鱼C工作室'])

# 字典类型
dict2 = {1: 'one', 2: 'two', 3: 'three'}
print(dict2)


print(dict2[2])

# 空字典
dict3 = {}
print(dict3)

# 查dict用法
help(dict)


# 键值对   字典


dict3 = dict((('F',70),('i',105),('s',115),('h',104),('c',67)))
print(dict3)
# 通过key加value的类型创建字典
dict4 = dict(小甲鱼='让编程改变世界',汉贼王='蒙西.D.罗杰')
print(dict4['汉贼王'])

print(dict4)

# 没有的
dict4['爱迪生'] = '天才是靠努力换来的'


# 类型（工厂函数）fromkeys
dict1 = {}
a = dict.fromkeys((1,2,3))
print(a)

a = dict1.fromkeys((1,2,3),'Number')
print(a)

# 修改值，会生成新的字典
dict1.fromkeys((1,3),'数字')

# 通过keys()  values()  items() 访问字典的值
dict1 = dict1.fromkeys(range(32),'赞')
print(dict1)

for eachkey in dict1.keys():
    print(eachkey)            # 所有的key 打印出来

for eachvalue in dict1.values():
    print(eachvalue)        # 所有的valie值

# 没有的会报错

# get方法
a = dict1.get(32)
print(a)         # 没有会返回None

#  成员操作符
a = 32 in dict1
print(a)

a = 31 in dict1
print(a)

# 字段里面查找的是元素的键
# 序列中查找的是值


dict1.clear()
print(dict1)


dict1 = {}
a = {'姓名':'小甲鱼'}
b=a
print(a)

a={}
print(a)

print(b)

# copy浅拷贝（拓展深拷贝）
a={1:'one',2:'two',3:'three'}
b=a.copy()    # 浅拷贝
c=a    # 赋值
print(a)
print(b)
print(c)

print(id(a))    # 查下地址
print(id(b))    # 地址不同
print(id(c))    # 直接赋值和源地址相同

c[4]='four'
print(a)
print(c)
print(b)      # 不受干扰

a.pop(2)      # 弹出元素
a.popitem()   # 随机从字典中弹出一个字、（1，'one'）


a.setdefault('小白')   # 在字典中找不到会自动添加，随机添加

a.update(b)
print(a)





