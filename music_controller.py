import urllib.request
from pydub import AudioSegment
from pydub.playback import play

# Download an audio file
urllib.request.urlretrieve("https://tinyurl.com/wx9amev", "metallic-drums.wav")

# Load into PyDub
loop = AudioSegment.from_wav("metallic-drums.wav")


# Repeat 2 times
loop2 = loop * 2
# Get length in milliseconds
length = len(loop2)
# Set fade time
fade_time = int(length * 0.5)
# Fade in and out
faded = loop2.fade_in(fade_time).fade_out(fade_time)

play(faded)

# Download another loop
urllib.request.urlretrieve("https://tinyurl.com/yx3k5kw5", "beat.wav")
# Load into PyDub
beat = AudioSegment.from_wav("beat.wav")
# Mix with our original loop
mixed = beat[:length].overlay(loop2)

play(mixed)

# Filter the beat at 3kHz
filtered = beat.low_pass_filter(3000)
# Mix loop2 with a reversed, panned version
loop = loop2.reverse().pan(-0.5).overlay(loop2.pan(0.5))
# Mix our filtered beat with the new loop at -3dB
final = filtered.overlay(loop2 - 3, loop=True)

play(final)
final.export("final.mp3", format="mp3")
