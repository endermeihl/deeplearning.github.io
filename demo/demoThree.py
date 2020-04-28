#!/usr/local/bin/python3.7
import numpy as np
x=np.array([[6,22,33,42,11],[2,3,4,12,12],[5,78,2,34,0]])
y=np.array([3,4,2,33,42])

def naive_relu(x):
    assert len(x.shape)==2
    
    x=x.copy()
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i,j]=max(x[i,j],0)
    return x

def naive_add(x,y):
    assert len(x.shape)==2
    assert x.shape==y.shape

    x=x.copy()
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i,j]+=y[i,j]
    return x

print(naive_relu(x))
print(naive_add(x,x))
print(x+x)

def naive_add_matrix_and_vector(x,y):
    assert len(x.shape)==2
    assert len(y.shape)==1
    assert x.shape[1]==y.shape[0]

    x=x.copy()
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i,j]+=y[j]
    return x

print(naive_add_matrix_and_vector(x,y))
