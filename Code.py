import pyttsx3                                     #pip install pyttsx3 and pip install pywin32
from googletrans import *                          #pip install googletrans
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)          #set male or female voice according to need - to change to female version edit-- voice[1].id
newVoiceRate = 120                                 #to control speed
engine.setProperty('rate',newVoiceRate)  
def speak(str):                                    #can be change to audio file to play audio in presentation
    engine.say(str)
    engine.runAndWait()                            #define timestamp
if __name__ == "__main__":
    a = input("Enter text here: \n")                   #enter text here
    t = Translator()
    k = t.translate(a, dest='language name')       #choose preffered language
    translated = str(k.text)
    speak(translated)
    
  
