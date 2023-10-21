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

def get_mili():
    return math.floor(time.time())

g = gTTS(text, lang=lang)
g.save(f'download/{get_mili()}.mp3')

print ('file saved to', f'download/{get_mili()}.mp3')
