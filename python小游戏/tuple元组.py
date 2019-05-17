# 元组和列表的不同，列表很灵活，元组不可改变
# 创建和访问一个元组和列表的区别
tuple1 = (1,3,4,5,6,7,9,0)
tuple1[1]

tuple1[5:]

tuple1[:5]

tuple2 = tuple1[:]
# tuple1[1] = 3     报错



temp = (1)
print(temp)    # 1
type(temp)   # <class 'int'>

temp2 = 2,3,4   # 元组
type(temp2)     # <class 'tuple'>

temp = []
type(temp)       # <class 'list'>

temp = ()
type(temp)        # <class 'tuple'>

temp = (1,)    #  temp = 1,
type(temp)       # <class 'tuple'>

print(8*(8))
print(8*(8,))   # 8个元组

# 切片创建一个新的元组
temp = ("小甲鱼",'黑夜','迷途','小布丁')
temp = temp[:2] + ('怡静',) + temp[2:]
print(temp)

del temp
# print(temp)      NameError

# 没有会被回收释放掉，拼接操作符，重复操作符，关系操作符，逻辑操作符




