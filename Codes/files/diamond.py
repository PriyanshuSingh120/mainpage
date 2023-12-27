n=int(input('Enter number of row :\n'))
for i in range(n-1):
    for j in range(i,n):
        print(' ', end=' ')
    for a in range(i):
        print('*', end=' ')
    for b in range(i+1):
        print('*', end=' ')
    print()
for x in range(n):
    for b in range(x+1):
        print(' ', end=' ')
    for v in range(x,n-1):
        print('*', end=' ')
    for f in range(x,n):
        print('*', end=' ')
    print()
