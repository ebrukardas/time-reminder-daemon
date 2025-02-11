
import gtts
from playsound import playsound # pip install playsound

# make request to google to get synthesis
tts = gtts.gTTS("Hello Ebru")

# save the audio file
tts.save("hello.mp3")

# play the audio file
playsound("hello.mp3")



# in spanish
tts = gtts.gTTS("Hola Mundo", lang="es")
tts.save("hola.mp3")
playsound("hola.mp3")