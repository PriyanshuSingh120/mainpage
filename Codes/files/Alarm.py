import time       #It import time fucntion in python
from playsound import playsound
import colorama        #It import color in python
from colorama import Fore
import sys
while True:
    Current_Time=time.strftime("%H:%M:%S", time.localtime()) #It takes current time
    print(Fore.LIGHTMAGENTA_EX+Current_Time+Fore.RESET)   # It print current time
    Alarm_Time=input(Fore.LIGHTBLUE_EX+'Enter the time at you apply alarm in 24 hours format: HH:MM:SS: '+Fore.LIGHTRED_EX)
    #Take input from user 
    hours=Alarm_Time[0]+Alarm_Time[1]    #It is hours of given input
    minute=Alarm_Time[3]+Alarm_Time[4]   #It is minutes of given input
    second=Alarm_Time[6]+Alarm_Time[7]   #It is Seconds of given input
    if int(hours)>=24 or int(minute)>=60 or int(second)>=60:
        print(Fore.LIGHTGREEN_EX+'Check your input\nincorrect input',Fore.WHITE)
        #If user set a wrong alarm it ask message and restart
        continue
    else:
         print(Fore.LIGHTCYAN_EX+'Alarm successfully set..'+Fore.RESET) #If time is right it print alarm successfully set  
         print(Fore.LIGHTYELLOW_EX+'your alarm ring at',Alarm_Time+Fore.RESET)  
    while 1:
        current_Time=time.strftime("%H:%M:%S", time.localtime()) #It is current time
        current_Hours=current_Time[0]+current_Time[1]   #It is current hours
        current_Miutes=current_Time[3]+current_Time[4]   #It is current minutes
        current_Seconds=current_Time[6]+current_Time[7]  #It is current second
        if hours==current_Hours and minute==current_Miutes and second==current_Seconds: #It check condition of time
            print(Fore.GREEN+'\rIt is ',Alarm_Time+Fore.RESET)
            print(Fore.LIGHTMAGENTA_EX+'Your time is over'+Fore.RESET) # It prints when time is over
            playsound('Alarm06.wav')    #It plays sound when time is over.
            break   #It breaks the loop
        else:
            sys.stdout.write(Fore.RED+'\rIt''\'s '+Fore.LIGHTMAGENTA_EX+current_Time+Fore.RESET)
            continue #If time is not correct it change current time
    Restart_loop=input(Fore.LIGHTGREEN_EX+'Do you want to set a new alarm: Yes/No: '+Fore.LIGHTRED_EX).lower() #It asks user to set a new alarm
    if Restart_loop!='yes':  #It check user want to restart loop
            print(Fore.MAGENTA+'See you Soon'+Fore.RESET)
            quit()
    else:
        print(Fore.LIGHTYELLOW_EX+'Okay Let''\'s\ set a new Alarm'+Fore.RESET)
        continue