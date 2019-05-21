def hello():
    print('hello FishC!')
temp = hello()
print(temp)    # 没有返回None

# return

def back():
    return [1, '小甲鱼', 3.14]

print(back())

# 默认返回元组
def back():
    return 1, '小甲鱼', 3.14
print(back())

# 局部变量和全局变量
def discounts(price, rate):
    final_price = price * rate
    return final_price

old_price = float(input("请输入原价："))
rate = float(input('请输入折扣率：'))
new_price = discounts(old_price,rate)
print('打折后的价格是：', new_price)
# 试图修改全局变量，试图修改，python会创建一个新的局部变量

def discounts(price, rate):
    final_price = price * rate
    # print('这里试图打印全局变量old_price的值:' old_price)
    old_price = 50
    print('修改后old_price的值是1:', old_price)
    return final_price
old_price = float(input('请输入原价：'))
rate = float(input('请输入折扣率：'))
new_price = discounts(old_price, rate)
print('修改后old_price的值是2：', old_price)
print('折扣后价格是：', new_price)
