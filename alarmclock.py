import time
from playsound3 import playsound

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}Alarm in: {minutes_left:02d}:{seconds_left:02d}")
    
    playsound("Bells01.mp3")

addminutes = int(input("How many minutes should the timer be? "))
addseconds = int(input("How many seconds should the timer be? "))

seconds = (addminutes * 60) + addseconds

alarm(seconds)