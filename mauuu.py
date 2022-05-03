import webbrowser
import pyttsx3
import os
import datetime
import speech_recognition as sr
from pyttsx3 import engine
import wikipedia 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():                                                                                                                                               
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning")

    elif hour>=12 and hour<=18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am Mauuu how may I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said: ",query,"\n")

    except Exception as e:
        print("Say again...")
        return "None"

    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()   
        
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")    

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")            

        elif 'open linkedin' in query:
            webbrowser.open("https://www.linkedin.com/in/anshikthakur55/.com")    

        # elif 'play music' in query:
        #     music_dr =     
        #     songs = os.listdir(music_dr)
        #     print(songs)
        #     os.startfile(os.path.join(music_dr, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%H:%S")
            speak("Time right now is ",strTime)

        elif 'open code' in query:
            codePath = "C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"    
            os.startfile(codePath)

        elif 'quit' in query:
            exit()