a = int(5.9)
print(a)     # 向下取整

# 四舍五入
# temp = input("输入一个浮点数：")
# floats = float(temp)
# ints = int(temp)      # invalid literal for int() with base 10: '6.5'
# if (floats - ints) >= 0.5:
#     f = floats + 1
#     print(f)
# else:
#     print(ints)


print(int(4.5 + 0.5))
print(int(4.3+0.5))

temp = input("不妨输入数字试试：")
while type(temp) != type(1):
    print("抱歉你输入的不合法", end='')
    temp = input("请输入合法整数：")

# temp = input("不妨输入数字试试：")
# while not isinstance(temp, int):
#     print("抱歉你输入的不合法", end='')
#     temp = input("请输入合法整数：")

'''
s 为字符串

s.isalnum()  所有字符都是数字或者字母，为真返回 True，否则返回 False。

s.isalpha()   所有字符都是字母，为真返回 True，否则返回 False。

s.isdigit()     所有字符都是数字，为真返回 True，否则返回 False。

s.islower()    所有字符都是小写，为真返回 True，否则返回 False。

s.isupper()   所有字符都是大写，为真返回 True，否则返回 False。

s.istitle()      所有单词都是首字母大写，为真返回 True，否则返回 False。

s.isspace()   所有字符都是空白字符，为真返回 True，否则返回 False。
         
例如：
>>> s = 'I LOVE FISHC'
>>> s.isupper()
>>> True
'''
# 写一个程序，判断给定年份是否为闰年

temp = input("请输入一个数字：")
while not temp.isdigit():
    temp = input("抱歉，输入数字有误，请输入一个整数：")

year = int(temp)
if year/400 == int(year/400):
    print(temp + '是闰年！')
else:
    if(year/4 == int(year/4) and (year/100 != int(year/100))):
        print(temp + '是闰年！')
    else:
        print(temp + '不是润年！')




