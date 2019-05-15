list = [1,[1,2,'小甲鱼'],3,5,8,13,18]

list[1][2]='小鱿鱼'
print(list)
reverse = [2,4,8,6,5,6]
print(sorted(reverse))
print(sorted(reverse))      # 逆序方法待开发学


list1 = [x**2 for x in range(10)]
print(list)

list1 = []
for x in range(10):
	list1.append(x**2)

list1 = [(x, y) for x in range(10) for y in range(10) if x % 2 == 0 if y % 2 != 0]


list1= []
for x in range (10):
    for y in range (10):
        if x%2 ==0 and y%2!= 0:
            list1.append((x,y))
print (list1)



old = [1, 2, 3, 4, 5]
new = old
old = [6]
print(new)      # [1, 2, 3, 4, 5]


list1 = [1, [1, 2, ['小甲鱼']], 3, 5, 8, 13, 18]
list1[1][2][0] = '小鱿鱼'


# 列表名.sort()
# 列表名.reverse()

# copy() 方法
list2 = list1.copy()
list2
[1, [1, 2, ['小甲鱼']], 3, 5, 8, 13, 18]

# clear() 方法
list2.clear()

# 推倒还原
list1 = [(x, y) for x in range(10) for y in range(10) if x % 2 == 0 if y % 2 != 0]


list = []
for x in range(10):
    for y in range(10):
        if x%2 == 0:
            if y%2 != 0:
                list.append((x, y))



