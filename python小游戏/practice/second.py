# 以下哪个变量的命名不正确？为什么？
myteacher = '小甲鱼'
yourteacher = myteacher
yourteacher = '黑夜'
print(myteacher)      # 小甲鱼

print(yourteacher)     # 黑夜

first = 520
second = '520'
first = second
print(first)       # 520

# 除了使用反斜杠（\）进行字符转义，还有什么方法可以打印：Let's go! 这个字符串
print("Let's go!")
print('Let\'s go')
print('''Let's go!''')

# 如果非要在原始字符串结尾输入反斜杠，可以如何灵活处理？
print("hello world\\")
# 变量命名，变量名包含字母，数字，下划线。不能以数字开头


# 要求使用变量，计算一年有多少秒？
DayPerYear = 365
HourPerDay = 24
MinutesPerHour = 60
SecondPerMinute = 60
YearMinute = DayPerYear * HourPerDay * MinutesPerHour * SecondPerMinute
print(YearMinute)


# 关于最后提到的长字符串（三重引号字符串）
string = '''

三重引号字符串
'''
print(string)
