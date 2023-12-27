import sys
import time
from colorama import Fore
from playsound import playsound 
while True:
    Input=input(Fore.LIGHTBLUE_EX+'Enter the time HH:MM:SS : '+Fore.LIGHTCYAN_EX)
    try:
        Hours_1=0
        Minutes_1=0
        Seconds_1=0
        Hours=int(Input[0]+Input[1])
        Minutes=int(Input[3]+Input[4])
        Seconds=int(Input[6]+Input[7])
        print(Fore.LIGHTRED_EX+'Timer Successfully Set..'+Fore.RESET)
    except ValueError:
        print(Fore.RED+'Invalid Input'+Fore.RESET)
        continue
    while 1:
        if Seconds_1==60:
            Minutes_1=Minutes_1+1
            Seconds_1=0
        if Minutes_1==60:
            Hours_1=Hours_1+1
            Minutes_1=Minutes_1-1
        if Hours_1==Hours and Minutes==Minutes_1 and Seconds==Seconds_1:
            print(Fore.LIGHTGREEN_EX+'\nTime end'+Fore.RESET)
            playsound('clock-alarm-8761.mp3')
            break
        else:
            Seconds_1= Seconds_1+1
            sys.stdout.write(Fore.LIGHTMAGENTA_EX+'\r'+str(Hours_1)+' : '+str(Minutes_1)+' : '+str(Seconds_1)+' Time left'+Fore.RESET)
            time.sleep(0.98899999999999999999)
            continue
    Restart_Input=input(Fore.LIGHTMAGENTA_EX+"Do you want to restart Loop: Yes/No: "+Fore.LIGHTWHITE_EX).capitalize()
    if Restart_Input=='Yes':
        continue
    else:
        print(Fore.LIGHTRED_EX+'Okay! See you Soon\n Thank You'+Fore.RESET)
        quit()