
# 每次执行就要进行重新判断
score = int(input("请输入一个分数："))
if 100 >= score >= 90:
    print('A')
if 90 > score >= 80:
    print('B')
if 80 > score >= 60:
    print('C')
if 60 > score >= 0:
    print('D')
if score < 0 or score >100:
    print('输入错误！')


score = int(input("请输入一个分数："))
if 100 >= score >= 90:
    print('A')
elif 90 > score >= 80:
    print('B')
elif 80 > score >= 60:
    print('C')
elif 60 > score >=0:
    print('D')
else:
    print("输入错误！")

# 避免悬挂else      强制缩进，减少不必要的错误
'''
if （hi > 2)
    if(hi > 7)
        printf("好棒！好棒！")；
else
    printf("切~");     
'''
# 条件表达式（三元操作符）
'''
x,y = 4,5
if x < y:
    small = x
else:
    small = y
改进
small = x if x < y else y
'''
# 断言（assert）
'''
当这个关键字后面的条件为假的时候，程序自动崩溃并抛出AssertionError的异常
assert 3 > 4
一般再程序中用Ta插入检查点，当需要确保程序中的某个条件一定为真才能让程序正常工作
assert 4 > 3     可忽略报错
'''

# request库  
