while True:
    a=input('Enter a number:')
    try:
        a=int(a)
    except ValueError:
        print(a,'is not Integer')
        continue
    i='0'
    for c in range(a):
        if(a%2==0):
            a=a/2
            i=i+"0"
        if(a%2==1):
            a=(a-1)/2
            i=i+'1'
        if a<=0:
            break
    for d in range(int(len(i))-1,0,-1):
        print(i[d],end=" ")
    c=input('\nDo you want one more conversion: yes/No: ').lower()
    if c !='yes':
        print('Thanks for comming\nSee You soon')
        quit()