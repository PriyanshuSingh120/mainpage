while True:
    from colorama import Fore
    print(Fore.LIGHTCYAN_EX+'program to convert Binary number to Decimal Number')
    Input=input(Fore.LIGHTGREEN_EX+'Enter a Binary number:'+Fore.LIGHTBLUE_EX)
    b=len(Input)
    a=int(Input)
    for c in range(b):
        d=int(Input[c])
        if(d>=2):
            print(Fore.RED+str(a) ,' is not a binary number'+Fore.RESET)
            break
    else:
        if(b==1):
            print(Fore.BLUE+str(int(Input)*1))
        if b==2:
            print(Fore.BLUE+str(int(Input[1])*1+int(Input[0])*2))
        if b==3:
            print(Fore.BLUE+str(str(int(Input[2])*1+int(Input[1])*2+int(Input[0])*4)))
        if b==4:
            print(Fore.BLUE+str(int(Input[3])*1+int(Input[2])*2+int(Input[1])*4+int(Input[0])*8))
        if b==5:
            print(Fore.BLUE+str(int(Input[4])*1+int(Input[3])*2+int(Input[2])*4+int(Input[1])*8+int(Input[0])*16))
        if b==6:
            print(Fore.BLUE+str(int(Input[5])*1+int(Input[4])*2+int(Input[3])*4+int(Input[2])*8+int(Input[1])*16+int(Input[0])*32))
        if b==7:
            print(Fore.BLUE+str(int(Input[6])*1+int(Input[5])*2+int(Input[4])*4+int(Input[3])*8+int(Input[2])*16+int(Input[1])*32+int(Input[0])*64))
        if b==8:
            print(Fore.BLUE+str(int(Input[6])*1+int(Input[5])*2+int(Input[4])*4+int(Input[3])*8+int(Input[2])*16+int(Input[1])*32+int(Input[0])*64+int(Input[0])*128))
        if(b>=9):
            print('Work in progress\nPlesae wait')
    Reinput=input(Fore.LIGHTMAGENTA_EX+'Do you want to restart: Yes/No: '+Fore.LIGHTBLUE_EX).capitalize()
    if Reinput!='Yes':
        print(Fore.RED+'See You Soon\nThank You'+Fore.RESET)
        break
    else:
        continue
    