# 集合
num={}
a=type(num)
print(a)

num2={1,2,3,4,5}
a=type(num2)
print(a)


num2={1,2,3,4,5,5,6,7,9,8,8}
print(num2)   #集合是唯一的
# 集合不支持索引

# 创建集合的两种方法；一直接用花括号括起来，二是使用set()工厂函数
set1=set([1,2,3,4,5,5])
print(set1)    # 自动剔除多余的元素


num1 = {1,2,3,4,5,6,6,6,7,2,1,0}
temp=[]
for each in num1:
    if each not in temp:
        temp.append(each)
print(temp)


num1=list(set(num1))
print(num1)       # set得到的集合是无序的


# 如何访问集合中的值
print(num2)

a=1 in num2
print(a)        # 1在集合中返回Ture

a='1' in num2
print(a)        # 字符串不在返回False

num2.add(6)     # 添加元素

num2.remove(5)    # 删除一个元素

# 不可变集合frozen
num3 = frozenset([1,2,3,4,5])
num3.add(0)
print(num3)      # 不可变集合





