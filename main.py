from gtts import gTTS  
from playsound import playsound  

text_val = "text"
language = 'en'

obj = gTTS(text=text_val, lang=language, slow=False)
obj.save("output.mp3")  

# Play saved sound file
playsound("output.mp3")