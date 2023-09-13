# What is this
This tool can be used to convert a String into morse code. 
The morse code can be played by the computer or a mp3 file can be created. 

# How do i Use it 
You have the 'main.py' file we can run this from the commandline. 
You need to provide a argument '--string' this string will be converted to a morse code. 

You can also provide further arguements '--export_file' and '--play_sound'. If not these values are not provided they will default to True. 

## Example
'''
python3 main.py --string "Hello World"

python3 main.py --string "I like python" --no-play_sound
python3 main.py --string "I like python" --no-export_file
'''

# Requirements 
- Pygame needs to be installed 
- pydub needs to be installed 