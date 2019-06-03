# 输入  处理    输出
# 什么是文件  .exe可执行文件；  .txt     .jpg图的格式       .mp4 .avi视频的格式
# open()
'''
'r'       open for reading (default)    只读
    'w'       open for writing, truncating the file first     没有创建个，有则覆盖原文件
    'x'       create a new file and open it for writing        
    'a'       open for writing, appending to the end of the file if it exists     追加文件
    'b'       binary mode        二进制
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    'U'       universal newline mode (deprecated)  通用换行符
    '''
f = open('C:\\record.txt')
print(f)
# 拓展：文件对象方法，文件打开模式
# f.close()关闭文件
# python会缓存你的写入文件，为安全使用后关闭文件
a=f.read()
print(a)
a=f.read()    # 类似书签，读到那，停止那
print(a)
f.read(5)

a=f.tell()     # 字节数
print(a)

a=f.seek(45, 0)
print(a)


a=f.readline()
print(a)


print(list(f))      #生成列表

# 生成一行行列表、
lines=list(f)
for each_line in lines:
    print(each_line)


f.seek(0,0)
for each_line in f:
    print(each_line)



# 写入文件，确保之前的文件
f = open('C:\\text.txt', 'w')
f.write("我爱你们")
f.close()
print(f)






