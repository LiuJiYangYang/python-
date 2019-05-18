# 序列
# help(list)   # list方法

b='I love you'
b=list(b)
print(b)

c=(1,1,2,3,5,8,13,21,34)
c=list(c)
print(c)

c=tuple(c)
print(c)

print(len(c))  # 长度


print(max(1,2,3,5,7))
print(max(b))

members = [1,17,13,0,-98,34,54,76,32]
print(max(members))

print(min(members))

tuple1 = (1,2,3,4,56,6,78,)
print(max(tuple1))
# 数据类型必须一致

'''
max = tuple1[0]

for each in tuple1:
    if each > max:
        max = each
        
return max
'''
tuple2=(2.3,4.5,6.7)
print(sum(tuple2))     # 数据类型必须一致

print(sum(members, 9))
print(sum(tuple2, 6))
# 字符串不能进行使用sum方法会报错

print(sorted(members) )      # 排序


reversed(members)    # 返回对象
list(reversed(members))


enumerate(members)    # 返回对象
print(list(enumerate(members)))

a=[1,2,3,5,6,7]
b=[1,2,3,4,5]
zip(a,b)     # 返回对象
print(list(zip(a,b)))