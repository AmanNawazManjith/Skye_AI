import code
from json.tool import main
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:    
        speak("Good Evening")

    
    speak("I am Skye Sir. Please tell me how may I help you")



def takeCommand():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('am5937@srmist.edu.in','Norman@1234')
    server.sendmail('vb7224@srmist.edu.in',to,content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        
        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia..') 
            query = query.replace("Wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open' in query:
            a=query.split()
            b=a[1]
            webbrowser.open(b+'.com')

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
             music_dir = 'E:\⚔️PewerRengers⚔️\\tunes'
             songs=os.listdir(music_dir)
             print(songs)
             os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, The time is {strTime}")
        elif 'who are you' in query:
            speak("I am Skye, your personal AI assistant.")
        
        elif 'bye' or 'quit' in query:
            speak("Shutting down sir, Thanks for your time.")
            exit()

        elif 'open code' in query:
            codePath = "C:\\Users\\amana\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'spotify app' in query:
            codePath = "C:\\Users\\amana\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(codePath)

        elif 'send an email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "vb7224@srmist.edu.in"
                sendEmail(to, content)
                speak("Your email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir, I am not able to send this email")
        




