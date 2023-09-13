from pygame import mixer 
import time

mixer.init()
short_beep =mixer.Sound("assets/morse_short.mp3")
long_beep = mixer.Sound("assets/morse_long.mp3")

def play_sound(morse_string:str): 
    for beep in morse_string:
        if beep == "-":
            mixer.Sound.play(long_beep)
            time.sleep(0.5)
        elif beep == ".":
            mixer.Sound.play(short_beep)
            time.sleep(0.5)
        else:
            time.sleep(1)
