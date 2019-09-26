data = [-1,2,3,-4,5]

res = []
for x in data:
    if x >=0:
        res.append(x)
print(res)

from random import randint

l = [randint(-10, 10) for _ in range(10)]

res = [x for x in l if x >=0]
res = list(filter(lambda x:x>=0,l))

d = {'student%d' % i:randint(50,100) for i in range(1,21)}

g2 = dict(filter(lambda x: x[1]>=90,d.items()))


g={k:v for k,v in d.items() if v>=90}

print(g)
print(g2)

s = {randint(0,20) for _ in range(20)}

sr= {x for x in s if x%3==0}
sr2 = list(filter(lambda x:x%3==0,sr))
print(sr)
print(sr2)

data2 =[randint(0,20) for _ in range(30)]
d = dict.fromkeys(data,0)


d = {k: randint(60, 100) for k in 'abcdefgh'}

l = [(v, k) for k, v in d.items()]
s=sorted(l, reverse=True) 

print(sorted(d.items(),key=lambda item:item[1],reverse=True))

from random import randint,sample
from functools import reduce

d1 = {k:randint(1,4) for k in sample('abcdefgh',randint(3,6))}
d2 = {k:randint(1,4) for k in sample('abcdefgh',randint(3,6))}
d3 = {k:randint(1,4) for k in sample('abcdefgh',randint(3,6))}
print(d1)
print(d2)
print(d3)
dl=[d1,d2,d3]
print([k for k in dl[0] if all(map(lambda d:k in d,dl[1:]))])

print(lambda a,b:a&b,map(dict.keys,dl))

print(list(map(dict.keys,dl)))
