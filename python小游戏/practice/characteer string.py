str1 = '''
此生何有声声叹，
断杯落残垣，
君不见，青山
浩劫终化成烟。
'''
print(str1)
str2 = '此生何有声声叹，\n' \
       '断杯落残垣，\n' \
       '君不见，青山\n' \
       '君不见，青山\n' \
       '浩劫终化成烟。\n'
print(str2)
str3 = ('此生何有声声叹，\n'
        '断杯落残垣，\n'
        '君不见，青山\n'
        '浩劫终化成烟。\n')
print(str3)
# 未实现，解决方案
# file1 = open('C:\windows\temp\readme.txt', 'r')
# file1 = open(r'C:\windows\temp\readme.txt', 'r')

# 分片
str1 = '<a href="http://www.fishc.com/dvd" target="_blank">'
print(str1[16:29])
print(str1[-45:-32])

print(str1[-36:20])     # 从左往右排在前面的索引方在':'左边后面的放在右边,不论正负


# 还原字符串
str1 = 'i2sl54ovvvb4e3bferi32s56h;$c43.sfc67o0cm99'
print(str1[::3])










