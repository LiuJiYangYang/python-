def list1():
    for each in list1():
        if each < min:
            min = each
    return each

# min Function

def min(x):
    least = x[0]
    for each in x:
        if each < least:
            least = each
    return x

# sum Function
def sum(x):
    result = 0
    for each in x:
        if (type(each) == int) or (type(each) == float):
            result += each
        else:
            continue
    return result

print(sum([1, 2.1, 2.3, 'a', '1', True]))


# 把可迭代的对象转换为列表、元组和字符串
temp = 'I love FishC.com!'
print(list(temp))
print(tuple(temp))
print(str(temp))


name = input("请输入待查找的用户名：")
score = [['迷途', 85], ['黑夜', 80], ['小布丁', 65], ['福禄娃娃', 95], ['怡静', 90]]
IsFind = False

for each in score:
    if name in each:
        print(name + '的得分是：',each[1])
        IsFind = True
        break
if IsFind == False:
    print('查找的数据不存在！')



















