# 条件为真就执行循环
'''
while 条件：
    循环体
'''

'''
for 目标 in 表达式：
    循环体
'''
favourite = 'Fishc'
for i in favourite:
    print(i, end=' ')

member = ['小甲鱼', '小布丁', '黑夜', '迷涂', '怡静']
for each in member:
    print(each, len(member))

for each in member:
    print(each,len(each))

'''
range([strat,] stop[,step=1])
从start开始到stop参数，step间隔
'''
range(5)
range(0, 5)
list(range(5))

for i in range(5):
    print(i)

for i in range(2, 9):
    print(i)

for i in range(1, 10, 2):
    print(i)
# break终止循环跳出循环体
'''
bingo = '小甲鱼是帅哥'
answer = input(’请输入小甲鱼最想听的一句话：')

while Ture：
    if answer == bingo:
        break
    aswer = input('抱歉，错了，请重新输入（答案正确才能退出游戏）：')
print('哎呦，帅哦~')
print('你真是小甲鱼肚子里的蛔虫啊！')
'''

for i in range(10):
    if i%2 != 0:
        print(i)
        continue
    i += 2
    print(i)