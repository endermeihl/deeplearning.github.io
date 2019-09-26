f = lambda x,y: x+y
print(f(1,2))

list_x = [1,2,3]

def square(x):
    return x * x

r = map(square,list_x)
print(list(r))

k = map(lambda x: x*x,list_x)
print(list(k))

## reduce函数
from functools import reduce

list_y = [1,2,3,4]
r = reduce(lambda x,y: x+y, list_y)
print(r)

m = reduce(lambda x,y: x+y, list_y, 10) # 10为初始值
print(m)

# filter 类
list_z = [1,0,1,0,1]
n = filter(lambda x: True if x==1 else False, list_z)
print(list(n)) 