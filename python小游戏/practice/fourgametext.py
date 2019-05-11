import random
times = 0
secret = random.randint(1, 10)  # 随机函数
print('猜字谜')
# 先给出guess赋值（赋一个绝对不等于secret的值）
guess = 0
# print()默认是打印完字符串会自动添加一个换行符，end=" "参数告诉print()用空格代替换行
print('猜猜我心里想的是什么数字？：', end='')
while (guess != secret) and (times < 3):
    tmep = input()
    guess = int(tmep)
    times = times + 1
    if guess == secret:
        print("wtf,你是我心里的蛔虫！")
    else:
        if guess > secret:
            print("大了，大量")
        else:
            print("小了小了")
        if times < 3:
            print("再试一次吧：", end='')
        else:
            print('机会用完了，退下吧！')
print('游戏结束，欢迎下次再来！')

print()


i = 10
while i:
    print("我爱吃鱼！")
    i = i - 1


rait = input("输入数字：")
cost = int(rait)
if 50 > cost > 10:
    print(cost)
# 一行写多个语句
print(), print()

print('i LOVE'); print('you')

print(
    'i love \n '
    'you'
)



