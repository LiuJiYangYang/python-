# 列表，混合列表
member = ['小甲鱼', '小布丁', '黑夜', '迷途', '恬静']
member = [1,2,3,4,5]

mix = [1, '小甲鱼', 3.14, [1,2,3]]

empty = []

# 添加再列表的尾部
member.append('小新')

# extendt添加一个列表的数据
member.extend(['呵呵', '来分'])

# insert指定添加
member.insert(1, ['红花'])

# 获取数组值
print(member[0])

# 赋值(调换位置)
temp = member[0]
member[0] = member[1]
member[1] = temp
print(temp)

# 从列表删除元素
member.remove('怡静')
print(member)         #  必须知道元素名字


# 删除列表
del member[1]
# del member

# 从列表中取出最后一个元素并返回给你
member.pop()

# 把pop取出的参数赋值给name
name = member.pop()
print(name)

member.pop(1)

# 列表分片（Slice）
member[1:3]      # 从索引1开始到3不包含三
# 列表本身未变

member[:]
member[1:]
member[:3]


member2 = member[:]






