while True:
    v=int(input('''
1. for Fraction Addtion
2. for Fraction Substraction
Enter your choice: 1/2: '''))
    if v in[1,2]:
        first=input("Enter Finrst Number in form of p/q : ")
        second=input("Enter Second Number in form of p/q : ")
        a=int(first[0])
        b=int(first[2])
        c=int(second[0])
        d=int(second[2])
        if b==0 or d==0:
            print('\n\t0 is not a rational number')
            continue
        e=b
        f=d
        n=1
        for m in range(1,e+f):
            if e%m==0 and f%m==0:
                e=e/m
                f=f/m
                n=n*m
            elif e%m==0 and f%m==0:
                e=e/m
                f=f/m
                n=n*m
            elif e%m==0 and f%m==0:
                e=e/m
                f=f/m
                n=n*m
            elif e%m==0 and f%m==0:
                e=e/m
                f=f/m
                n=n*m
            elif e%m==0 and f%m==0:
                e=e/m
                f=f/m
                n=n*m
            elif e%m==0 and f%m==0:
                e=e/m
                f=f/m
                n=n*m
            g=n*e*f
        h=(g/b)*a
        i=(g/d)*c
        if v==1:
            print(h+i,'/',g)
        elif v==2:
            print(h-i,'/',g)
    if v>2:
        print('incorrect Input')
    z=input('Do you want a new calculation: Yes/No: ').lower()
    if z !='yes':
        print('See you Soon\nThanks for Comming\n')
        quit()
    
