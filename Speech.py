import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS

def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("start audio.mp3")

def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data

def jarvis(data):
    if "hi how are you" in data:
        speak("I am fine how are you")

    if "what time is it" in data:
        speak(ctime())

    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on Anne, I will show you where " + location + " is.")
        os.system("chrome-browser https://www.google.dk/maps/place/" + location + "/&amp;")
    if "I am good" in data:
        speak("Nice to hear you are doing good")
    if "can I ask you a question" in data:
        speak("sure what is your question")





def jarviss(data):
    if "hi how are you" in data:
        speak("I am fine how are you")

    if "what time is it" in data:
        speak(ctime())
    if "I am good" in data:
        speak("Nice to hear you are doing good")
    if "can I ask you a question" in data:
        speak("sure what is your question,  i will ask my friend chat GPT")
    if "my question is" in data:
        speak("He says....")
# initialization
time.sleep(2)
speak("Hi , how can I help you?")
while 1:
    data = recordAudio()
    jarviss(data)
