import random
secret = random.randint(1,10)

print("小游戏")
game = input("输入整数数字：")
guess = int(game)
while guess !=secret:
    game = input("Guess again or Take another again：")
    guess = int(game)
    if guess == secret:
        print("verygood!")
        print("请在接再利")
    else:
        if guess >= secret:
            print("e大了")
        else:
            print("小了")
print("游戏结束")

# 第一次猜没有提示
# 第一次猜中没有恭喜

