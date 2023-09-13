from manage_morse import convert_string_to_morse
import sound
clear_input = input("Bitte geben Sie hier ihren Text ein:")

morse_string = convert_string_to_morse(clear_input)
sound.play_sound(morse_string)

sound.create_mp3(morse_string)
