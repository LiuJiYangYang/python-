# python的函数可以嵌套，但是要注意一下访问的作用域问题哦，
# 请问一下代码存在什么问题
def outside():
    print('I am outside!')
    def inside():
        print('I am inside!')
# inside()
# 访问的作用域问题，outside可以调用inside，
# 但是不能从外面或者别的函数体里调用

# 代码A
def outside():
    var = 5
    def inside():
        var = 3
        print(var)
    inside()
outside()

# 代码B
'''
def outside():
    var = 5
    def inside():
        print(var)      # 报错
        var = 3
    inside()
outside()
'''
# 如何访问funln()
def funOut():
    def funln():
        print('宾馆！你成功访问到我啦！')
    return funln()
# 直接访问funOut(),返回的是funIn()函数

# 如何访问funIn()
def funOut():
    def funIn():
        print('宾果！你成功访问到我啦！')
    return funIn
# 这里需要用funOut()()访问
# 也可以曲线救国，go = funOut() ，然后访问go()


def funX():
    x=5
    def funY():
        nonlocal x
        x+=1
        return x
    return funY
a=funX()
print(a())
print(a())
print(a())
# 当a=funX()的时候，只要a变量没有被重新赋值
# funX()就没有被释放，也就是说局部变量x就没有被重新初始化
# 所以当全局变量不适用的时候，可以考虑使用闭包更稳定和安全



# 统计下边这个长字符串中各个字符出现的次数并找到小甲鱼送给大家的一句话
str1 = '拷贝过来的字符串'
list1 = []
for each in str1:
    if each not in list1:
        if each == '\n':
            print('\\n', str1.count(each))
        else:
            print(each, str1.count(each))
        list1.append(each)

# 找到字符串中的密码，1）每位密码为单个小写字母，2）没为密码的左右两边均有且只有三个大写字母
str1 = '拷贝过来的字符串'
countA = 0
countB = 0
countC = 0
length = len(str1)
for i in range(length):
    if str1[i] == '\n':
        continue
    if str1[i].isupper():
        if countB == 1:
            countC += 1
            countA = 0
        else:
            countA += 1
        continue
    if str1[i].islower() and countA==3:
        countB = 1
        countA = 0
        target = i
        continue
    if str1[i].islower() and countC==3:
        print(str1[target], edn='')
    countA = 0
    countB = 0
    countC = 0




























































