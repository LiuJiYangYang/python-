# lambda表达式
# lambda
lambda x,y:x+y

g = lambda x,y:x+y
print(g(3,4))


# filter过滤器
# help(filter)

filter(None,[1,0,False,True])


list(filter(None,[1,0,False,True]))


def odd(x):
    return x%2

temp = range(10)
show = filter(odd,temp)
print(list(show))

list(filter(lambda x:x%2,range(10)))



# 映射map
a = list(map(lambda x:x*2,range(10)))

print(a)






