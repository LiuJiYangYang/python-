str = "{{1}}".format("不打印","打印")
print(str)


str1 = "{0} love {1}.{2}".format("I", "FishC", "com")
print(str1)


str2 = "{a} love {b}.{c}".format(a='I', b='FishC', c="com")
print(str2)

str3 = '{0}{1:.2f}'.format('Pi= ', 3.1415)
print(str3)

# 进制转化，十进制转换二进制用bin()
q = True
while q:
    num = input('请输入一个整数(输入Q结束程序)：')
    if num != 'Q':
        num = int(num)
        print('十进制 -> 十六进制 : %d -> 0x%x' % (num, num))
        print('十进制 -> 八进制 : %d -> 0o%o' % (num, num))
        print('十进制 -> 二进制 : %d -> ' % num, bin(num))
    else:
        q = False

temp = input('请输入一个整数（输入Q结束程序）：')
while temp!='Q':
    a = hex(int(temp))
    b = oct(int(temp))
    c = bin(int(temp))
    print('十进制->十六进制：',temp,'->',a)
    print('十进制->八进制：',temp,'->',b)
    print('十进制->二进制：',temp,'->',c)
temp = input("请输入一个整数（输入Q结束程序）：")









