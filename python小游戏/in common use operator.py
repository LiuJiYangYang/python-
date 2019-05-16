#
list1 = [123]
list2 = [234]
print(list1 > list2)

list1 = [123, 456]
list2 = [234, 123]
print(list1 > list2)     # 从第零个元素开始比较，不成了直接返回False，后面不做比较

list3 = [123, 456]
(list1 < list2) and (list1 == list3)   #  Ture

list4 = list1 + list2
print(list4)

# 连接操作符不能实现添加功能
# 添加
list3 * 3

list3 *= 3

list3 *= 5


"河马" not in list3      # Ture

123 not in list3   # Flase


list5 = [123, ['小甲鱼', '牡丹'], 456]
'小甲鱼' in list5     # False
'小甲鱼' in list5[1]    # Ture
list[1][1]


# 列表类型的内置函数
dir(list)          # 各种方法
list3.count    # 方法解释

list3.count(123)   # 123在list中出现的次数

# index索引
list3.index(123)     # 第一个出现索引的位置

list3.index(123,3,7)   # 从索引第三未开始123 出现的位置


# reverse翻转
list3.reverse()

# sort排序
list6 = [4, 2, 5, 1, 6, 23]
list6.sort()      # 从小到大排序
list6.reverse()   # 从大到小排

# sort(func,key)算法课外拓展
list6.sort(reverse=True)     # 倒序

list7 = list6[:]     # 拷贝成新的

list8 = list6       # 赋予
list6.sort()  #  排序
print(list7)      # 不变
print(list8)     # 同list6 一样进行重新排序

# python3开始next()方法为__next__()
tuple1 = (x**2 for x in range(10))
tuple1 = (x**2 for x in range(10))
tu = tuple1.__next__()
tu1 = tuple1.__next__()
tu2 = tuple1.__next__()
tu3 = tuple1.__next__()
tu4 = tuple1.__next__()
tu5 = tuple1.__next__()
print(tu)
print(tu1)
print(tu2)
print(tu3)
print(tu4)
print(tu5)

# 转换
L = []
for i in range(10):
    L.append(i**2)




