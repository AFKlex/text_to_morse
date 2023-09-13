from pygame import mixer 
import time
from pydub import AudioSegment


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


def create_mp3(morse_string:str):
    combined_audio = AudioSegment.empty()
    for beep in morse_string:
        if beep == "-":
            combined_audio += AudioSegment.from_file("assets/morse_short.mp3")
            combined_audio += AudioSegment.silent(duration=500)
        elif beep == ".":
            combined_audio += AudioSegment.from_file("assets/morse_long.mp3")
            combined_audio += AudioSegment.silent(duration=500)
        else:
            combined_audio += AudioSegment.silent(duration=1000)

    combined_audio.export("output_audio.mp3", format="mp3")
