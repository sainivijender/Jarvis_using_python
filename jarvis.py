from logging import exception
from unittest import result
from pip import main
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishME():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning!")

    elif hour >= 12 and hour < 18:
        speak("good afternoon")

    else:
        speak("good evening")

    speak("I am jarvis sir. please tell me how may i help you")


def takecommand():
    # it take microphone input from user and return output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except exception as e:
        # print(e)
        print("say that again please....")
        return "none"
    return query


if __name__ == "__main__":
    wishME()
    while True:
        query = takecommand().lower()

        # Logic for executing task based query
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open study material' in query:
            webbrowser.open("google.com")
        speak("this is all you need sir for good marks")
