for i in range(0,10):
    for x in range(0,i):
        print('*',end='')
    print()

for i in range(0,10):
    for x in range(i,10):
        print(' ',end='')
    for y in range(0,i):
        print('*',end='')
    print()