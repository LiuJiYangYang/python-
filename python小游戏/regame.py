# 给提示，随机，三次机会
'''
>
>=
<
<=
==
!=
'''

print(1 > 3)
# if else 语句

print("小游戏")
game = input("输入整数数字：")
guess = int(game)
while guess !=8:
    game = input("Guess again or Take another again：")
    guess = int(game)
    if guess == 8:
        print("verygood!")
        print("请在接再利")
    else:
        if guess >= 8:
            print("e大了")
        else:
            print("小了")
print("游戏结束")

# while循环

# 使用and逻辑操作符

3>2 and 3<2

(5>3) and (4<3)

# 每次运行程序产生的答案随机的
# random模块             Modile 模块编程






