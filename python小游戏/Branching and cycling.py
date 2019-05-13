
not 1 or 0 and 1 or 3 and 4 or 5 and 6 or 7 and 8 and 9
(not 1) or (0 and 1) or (3 and 4) or (5 and 6) or (7 and 8 and 9)

print(0 or 0 or 4 or 6 or 9)   # 4


# 还记得我们上节课那个求闰年的作业吗？如果还没有学到“求余”操作，
# 还记得用什么方法可以“委曲求全”代替“%”的功能呢？
year = 32445
a= year / 4
b=year-4*a
if (b==0):
    print("闰年")
else:
    print("不是润年")

# 请写一个程序打印出 0~100 所有的奇数。
for i in range(1,100,2):
    print(i)

i=1
while i<=100:
    if(i%2):
        print(i)
        i+=1
    else:
        print("end")



# 我们说过现在的 Python 可以计算很大很大的数据，但是......真正的大数据计算可是要靠刚刚的硬件滴，不妨写一个小代码，让你的计算机为之崩溃？
# print(3**2**32)     超常计算

# 爱因斯坦曾出过这样一道有趣的数学题：有一个长阶梯，若每步上2阶，最后剩1阶；若每步上3阶，最后剩2阶；若每步上5阶，最后剩4阶；若每步上6阶，最后剩5阶；只有每步上7阶，最后刚好一阶也不剩
num = 0
while 1:
    if(num%2==1 and num%3==2 and num%5==4 and num%6==5 and num%7==0):
        print(num)
    else:
        num+=1
















