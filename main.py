import sys
from manage_morse import convert_string_to_morse
import sound
import argparse

def main ():
    parser = argparse.ArgumentParser(description='Python Converter to Morse')
    parser.add_argument('--string', type=str,required=True , help='The input String which should be converted.')
    parser.add_argument('--export_file', type=bool, default=True, help='Export the Morse Code as a MP3 File.')
    parser.add_argument('--play_sound', type=bool, default=True, help='Play the morse code at the computer.') 

    args = parser.parse_args()

    morse_string = convert_string_to_morse(args.string)
    if(args.play_sound):
        sound.play_sound(morse_string)
    if(args.export_file):
        sound.create_mp3(morse_string)


if __name__ == "__main__":
    main()