from gtts import gTTS
import os
mytext = 'a b c d e'
language = 'en'
myobj = gTTS(mytext, lang=language, slow=False)

myobj.save('welcome.mp3')
os.system("welcome.mp3")
