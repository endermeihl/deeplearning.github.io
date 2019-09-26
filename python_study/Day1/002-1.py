x = int(input('x='))
y = int(input('y='))

def eca(x,y):
    if x==y:
        return x
    if x<y:
        x,y=y,x
    return eca(x-y,y)
maxdivisor=eca(x,y)
minmultiple=x*y/maxdivisor

print('最大公倍数是%d' % maxdivisor)
print('最小公约数是%d' % minmultiple)