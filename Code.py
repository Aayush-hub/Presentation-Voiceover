import pyttsx3                                     #pip install pyttsx3 and pip install pywin32
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)          #set male or female voice according to need - to change to female version edit-- voice[1].id
def speak(str):                                    #can be change to audio file to play audio in presentation
    engine.say(str)
    engine.runAndWait()                            #define timestamp
if __name__ == "__main__":
    speak(" ")                                     #enter text here
