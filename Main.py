import sys
from datetime import datetime

def digitalClock():
    pm_am = "am"
    print("Digital Clock in python:)")
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        if int(current_time[:2]) > 12:
            current_time = current_time.replace(current_time[:2],str(int(current_time[:2]) - 12))
            pm_am = "pm"
        else:
            pm_am = "am"
        sys.stdout.write("\r"+str(current_time)+" "+pm_am)
        sys.stdout.flush()

digitalClock()

