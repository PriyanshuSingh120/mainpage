from colorama import Fore
print(Fore.LIGHTCYAN_EX+'''
1. for Addition
2. for subtraction
3. for multiplication
4. for division
5. for square root
6. for squre
''')
while True:
    a= int(input(Fore.LIGHTGREEN_EX+'Enter Your choise: 1/2/3/4/5/6: '+Fore.LIGHTBLUE_EX))
    if a in (1,2,3,4,5,6):
        if(a==1):
            b=float(input(Fore.LIGHTMAGENTA_EX+'Enter first number:'+Fore.LIGHTBLUE_EX))
            c=float(input(Fore.LIGHTMAGENTA_EX+'Enter second number:'+Fore.LIGHTBLUE_EX))
            print(Fore.LIGHTYELLOW_EX+'Answer=',b+c)
        if(a==2):
            d=float(input(Fore.LIGHTMAGENTA_EX+'Enter first number:'+Fore.LIGHTBLUE_EX))
            e=float(input(Fore.LIGHTMAGENTA_EX+'Enter second number:'+Fore.LIGHTBLUE_EX))
            print(Fore.LIGHTYELLOW_EX+'Answer =',d-e)
        if(a==3):
            d=float(input(Fore.LIGHTMAGENTA_EX+'Enter first number:'+Fore.LIGHTBLUE_EX))
            e=float(input(Fore.LIGHTMAGENTA_EX+'Enter second number:'+Fore.LIGHTBLUE_EX))
            print(Fore.LIGHTYELLOW_EX+'Answer =',d*e)
        if(a==4):
            d=float(input(Fore.LIGHTMAGENTA_EX+'Enter first number:'+Fore.LIGHTBLUE_EX))
            e=float(input(Fore.LIGHTMAGENTA_EX+'Enter second number:'+Fore.LIGHTBLUE_EX))
            print(Fore.LIGHTYELLOW_EX+'Answer =',d/e)
        if(a==6):
            d=float(input(Fore.LIGHTMAGENTA_EX+'Enter a number:'+Fore.LIGHTBLUE_EX))
            print(Fore.LIGHTYELLOW_EX+'square =',d*d)
        if(a==5):
            d=int(input(Fore.LIGHTMAGENTA_EX+'Enter a number:'+Fore.LIGHTBLUE_EX))
            for c in range(1,int(d/2)):
                if(c*c==d):
                    print(Fore.LIGHTYELLOW_EX+'Square root = ',c)
                else:
                    print('Square root for this number is not valid\nTry again')
    z=input(Fore.LIGHTWHITE_EX+'Do you want a new conversion: Yes/No: '+Fore.LIGHTBLUE_EX).upper
    if z=='YES':
        continue
    elif z !="YES":
        print(Fore.RED+'See you soon\n We saw you later\n\tThanks for using our code'+Fore.RESET)
        break


    