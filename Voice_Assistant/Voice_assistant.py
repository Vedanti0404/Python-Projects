# """
# pyttsx3 = python text ot speech
# speech_recognition =used to convert spoken words to the text and worls on APIs
# automate_wikipedia = used to automate and work on wikipedia
# smtplib = sending emails.
# webbrowsers =used to automate webbrowser
# os = used to work/ interact with os.
# datetime = used to work with date and time.

# """

import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id) #1 for female voice, 0 for male voice

def speak(audio):
    engine.say(audio) #take up audio
    engine.runAndWait() # text is converted then it will wait to convert.

def wishme():
    hour = int(datetime.datetime.now().hour) #to take time in hours in order to deccide whether it is the morning or the night. in 24 hour format
    if hour>=0 and hour<=12:
        speak("Good morning !")
    elif hour>=12 and hour<=18:
        speak("Good afternoon !")
    else:  # speak to speak 
        speak("good evening !")
    speak("How can I help you today?")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening to you Vedanti...")
        speak("Listening to you Vedanti")
        r.pause_threshold = 1# wait for 1 second before printing this below
        audio =r.listen(source)
    
    try:
        print("Recognizing your voice...")
        query = r.recognize_google(audio, language="en-in")
        print(f"You said : {query}\n")
    except Exception as e:
        print("Say that again ...")
        return "None"
    
    return query

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.email.com",587)
    server.ehlo()
    server.starttls()
    server.login("abc010203@gmail.com","abc@1234")     #put ur mail id and password
    server.sendmail("abc010203@gmail.com",to,content)
    server.close()

if __name__== "__main__":
    wishme()

    while True:
        query =takecommand().lower()

        if "wikipedia" in query:
            speak("searching wikipedia...")
            query =query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 5)
            speak("according to the wikipedia ")
            print(results)
            speak(results)

        if "open code" in query:
            npath="C:\\Users\\MY PC\\AppData\\Local\\Programs\\Microsoft VS Code"
            os.startfile(npath)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "google" in query:
            webbrowser.open("google.com")
        
        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Time is :{strTime}\n")

        elif "whatsapp" in query:
            webbrowser.open("webwhatsapp.com")