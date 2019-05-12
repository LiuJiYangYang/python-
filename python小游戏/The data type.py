# 整数；布尔，字符串，浮点，
# int，Ture，Flase,strint,float
# 整型，非整型
a = 0.00000000000000000000025
print(a)        # 2.5e-22
b = 10000000000000000000
print(b)
print(1e10)

# e记法     1.3e-10
#           1.3e10

# 运行

print(True + True)
print(True + False)
print(True * False)
# print(True / False)   # division by zero

a = '520'
b = int(a)
print(b)
# b = int("我爱你")  #  报错

a = "520"
b = float(a)      # 转换为浮点型

a = 530
b = float(a)      # 整型转换为浮点型

a = 5.99
b = str(a)     # 转换为字符串

c = str(5e19)       # 转换为字符串

# 赋值后再次赋值会报错
str = "I love FishC.com"

# 获取关于数据类型的信息
# isinstance(a, str)    返回布尔值
isinstance(2324.555, float)
isinstance(True, bool)
print(isinstance(1, bool))      #  返回Flase
# type()     # 函数
type(a)      # sting
type(5.2)   # float
type(True)   # 布尔
type(5e15)    # float
a = int(5.7)
print(a)




