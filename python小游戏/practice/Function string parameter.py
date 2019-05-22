# 下面程序会输入什么
def next():
    print('我在next（）函数里...')
    pre()

def pre():
    print('我在pre(）函数里...')

next()
# 我在next（）函数里...
# 我在pre(）函数里...

# 函数的返回值
def hello():
    print('hello fishC!')
# 没有return返回值，返回的是None；python所有的函数都有返回值


# python的return语句可以返回多个不同类型的值
# 默认使用元组形式返回，也可以用列表包含起来返回

# return x,y,'123','我爱你'
# return [x,y,'123','我爱你']

def fun(var):
    var = 1314
    print(var, end='')

var = 520
fun(var)    # 1314
print(var)   # 520


var = 'Hi'
def fun1():
    global var
    var = 'Baby'
    return fun2(var)

def fun2(var):
    var+='I love you'

def fun3(var):
    var = '小甲鱼'

print(fun1())     # Baby I love you

# 编写一个函数，判断传入的字符串参数是否为‘回文联’
# 回文联即用回文形式携程的对联，既可顺读，也可倒读。例如：上海自来水来自海上

# 回文联
def huiweilian(duilian):
    list1=[]
    for each in duilian:
        list1.append(each)
    list2=list1[:]
    list1.reverse()
    if list1==list2:
        print('是回文联')
    else:
        print('不是回文联')

var = input('请输入对联：')
huiweilian(var)


# 编写一个函数，分别统计出传入字符串参数
# 可能不止一个参数）的英文字母、空格、数字和其他字符的个数。

def type_count(*string):
    length=len(string)
    for i in range(length):
        letters=0
        digit=0
        space=0
        others=0
        for each in string[i]:
            if each.isalpha():
                letters+=1
            elif each.isdigit():
                digit+=1
            elif each == '':
                space+=1
            else:
                others+=1
        print('第%d个字符串有%d个字母，%d个数字，%d个空格，%d个其他字符' %(i+1,letters,digit,space,others))

type_count('I love fishC.com.','i love you, you love me.')













