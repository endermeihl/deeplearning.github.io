def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)

print(fact(10))


def add(arr):
    if len(arr)==0:
        return 0
    else:
        return arr.pop(0)+add(arr)
        

print(add([1]))