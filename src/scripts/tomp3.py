import sys
from gtts import gTTS
import time
import math

if len(sys.argv) < 3:
    raise Exception("Missing arguments. Usage: `tomp3 <text_file> <lang>`")

textfile = sys.argv[1]
lang = sys.argv[2]

with open(textfile, "r") as f:
    text = f.read()

def get_name():
    mili = math.floor(time.time() * 1000)
    beginning = text.split()[0]
    if len(beginning) > 10:
        beginning = beginning[:10]
    return f'{beginning}_{mili}.mp3'

g = gTTS(text, lang=lang)
mp3_name = get_name()
g.save(f'download/{mp3_name}')

print (f'download/{get_name()}.mp3')
