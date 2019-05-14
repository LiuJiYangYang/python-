# 下面的循环会打印多少次"I Love FishC"？
for i in range(0,10,2):
    print('I Love FishC')
# 5次

# 下面的循环会打印多少次"I Love FishC"？

'''
for i in 5:
    print('I Love FishC')
'''
# 会报错，上节课的课后习题我们提到了 in 是“成员资格运算符”，而不是像 C 语言那样去使用 for 语法。
# Python 的 for 更像脚本语言的 foreach。

while True:
    while True:
        break
        print(1)
    print(2)
    break
print(3)     # 打印出：2     3



