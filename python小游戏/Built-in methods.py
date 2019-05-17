str1 = 'I love fishC.com'

str1[:6]

str1[5]

str1[:6] + '插入的字符串' + str1[6:]   # 生成新的字符串


str1 = str1[:6] + '插入的字符串' + str1[6:]


str2 = 'xiaoxie'

str2.capitalize()  # 首字母大写

str2.casefold()     # 所有小写

str2.center()   # 居中

str2.count('x')     #  次数


str3 = 'I\tlove\tfishC.com'
str3.expandtabs()       # \t默认8个空格

str3.find('efc')    # 找不到返回-1，找到返回索引值

str4 = '雄安'
str4.lower()       # 返回Flase

str5 = 'Fishc'        # 首字母大写其他小写返回Ture
str5.istitle()   # 标题化

str5.join('12345')        # 填充


str.Istrip()       # 忽略空格


str.replace('fishc','xo')  # 替换

str.rfind()       # 从右边开始查找

str.split()     # 默认切空格   ，生成列表

str.strip()       # 去掉左右空格，指定去字符

str.swapcase()    # 大小写转换

str.translate(str.maketrans('s','b'))     # 替换








