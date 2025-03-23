from datetime import datetime
from playsound import playsound
alarmTime = input("enter the time of alarm(HH:MM:SS\n")
alarmHour=alarmTime[0:2]
alarmMinute=alarmTime[3:5]
alarmSecond=alarmTime[6:8]
alarmPeriod=alarmTime[9:11].upper()
print("setting up alarm...")
while True:
    now = datetime.now()
    currentHour=now.strftime("%I")
    currentMinute=now.strftime("%M")
    currentSecond=now.strftime("%S")
    currentPeriod=now.strftime("%p")
    if(alarmPeriod == currentPeriod):
        if(alarmHour == currentHour):
            if(alarmMinute == currentMinute):
                if(alarmSecond == currentSecond):
                    print("alarm is now!")
                    playsound('audio.mp3') #importing the audio here
                    break
