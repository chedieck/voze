import sys
from gtts import gTTS
import time
import math
import string
import json

with open('src/config.json', 'r') as file:
    config = json.load(file)
max_length = config.get('maxLength', 0)

if len(sys.argv) < 3:
    raise Exception("Missing arguments. Usage: `tomp3 <text_file> <lang>`")

textfile = sys.argv[1]
lang = sys.argv[2]

with open(textfile, "r") as f:
    text = f.read()
    if len(text) > max_length:
        raise Exception(f"Text exceeds {max_length} limit")

def get_name():
    mili = math.floor(time.time() * 1000)
    beginning = text.split()[0]
    if len(beginning) > 10:
        beginning = beginning[:10]
    beginning = ''.join([c for c in beginning if c not in string.punctuation])
    return f'downloads/{beginning}_{mili}.mp3'

g = gTTS(text, lang=lang)
mp3_name = get_name()

g.save(mp3_name)
print (mp3_name)
