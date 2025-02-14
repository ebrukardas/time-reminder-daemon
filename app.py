import pyttsx3
import time
from datetime import datetime

SECONDS_PER_MINUTE =    60
MINUTES_PER_HOUR =      60
CLOSE_TO_HOUR =         SECONDS_PER_MINUTE*(MINUTES_PER_HOUR-1) # 20

def text_to_sound(time):
    engine = pyttsx3.init()
    engine.say(f"REMINDER: It is {time.hour} o'clock!")
    engine.runAndWait()
    return

def check_time(START_HOUR=0, END_HOUR=24):
    while True:
        now = datetime.now()
        # print(now)
        if START_HOUR <= now.hour < END_HOUR and now.minute == 0:
            text_to_sound(now)
            time.sleep(CLOSE_TO_HOUR)
        else:
            # print("Not yet!")
            time.sleep(10)


# check_time(START_HOUR=7, END_HOUR=17)
# check_time()

if __name__ == "__main__":
    check_time()