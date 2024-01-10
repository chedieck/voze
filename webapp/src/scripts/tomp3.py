import sys
import time
import math
import string
import json
from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
from IPython.display import Audio


with open('src/config.json', 'r') as file:
    config = json.load(file)
max_length = config.get('maxLength', 0)

if len(sys.argv) < 3:
    raise Exception("Missing arguments. Usage: `tomp3 <text_file> <lang>`")

textfile = sys.argv[1]
lang = sys.argv[2]
text = 'Example text'

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

mp3_name = get_name()

print(mp3_name)

# download and load all models
preload_models()

audio_array = generate_audio(text)

# save audio to disk
write_wav("bark_generation.wav", SAMPLE_RATE, audio_array)
  
# play text in notebook
Audio(audio_array, rate=SAMPLE_RATE)
