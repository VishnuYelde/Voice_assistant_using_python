import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import os
import wolframalpha
import requests
import json
from ecapture import ecapture as ec
import subprocess


#print('I am your personal assistant, go ahead')
#talk('I am your personal assistant, speak, go ahead')

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
print('I am your personal assistant, go ahead')



    
def talk(text):
    engine.say(text)
    engine.runAndWait()

    
    
def wishMe():
   hour=datetime.datetime.now().hour
   if hour>=0 and hour<12:
       talk("Hello,Good Morning")
       print("Hello,Good Morning")
   elif hour>=12 and hour<18:
       talk("Hello,Good Afternoon")
       print("Hello,Good Afternoon")
   else:
       talk("Hello,Good Evening")
       print("Hello,Good Evening")


print("Speak Now")
           
def takecommand():
    try:
        with sr.Microphone() as source:
            
            print('listening....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            engine.say(command)
            if 'alexa' in command:
                command = command.replace('alexa','')
                print(command)
    except Exception as e:
        talk("sorry, please say that again")
        return "None"
    return command


def run_alexa():
    talk('I am your personal assistant, go ahead')
    wishMe()

    command =takecommand()
    print(command)
    
    if "goodbye" in command or "shutdown" in command or "okay bye" in command or "stop" in command:
            print('your alexa is shutting down,Good bye')
            talk('your alexa is shutting down,Good bye')
            exit()
    
    elif 'open youtube' in command:
        talk("Here you go to Youtube\n")
        webbrowser.open("youtube.com")


    elif 'open google' in command:
        talk("Here you go to Google\n")
        webbrowser.open("google.com")

    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is' + time)
        
    elif "today's date" in command:
        date = datetime.datetime.now().strftime('%d/%m/%Y')
        print(date)
        talk(date)
        
    elif 'who are you' in command or 'what can you do' in command:
        talk('I am Alexa version 1 point O your persoanl assistant. I am programmed to minor tasks like'
                 'opening youtube, google chrome, gmail and play songs, predict time,take a photo,search wikipedia,predict weather' 
                 'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')    

    elif 'what' in command or "who" in command:
        talk('Searching Wikipedia...')
        command = command.replace('what','')
        command = command.replace('who','')
        info = wikipedia.summary(command, 3)
        talk("According to Wikipedia")
        print(info)
        talk(info)
        
    elif "where" in command or "when" in command:
        talk('Searching Wikipedia...')
        command = command.replace('where','')
        command = command.replace('when','')
        info = wikipedia.summary(command, 3)
        talk("According to Wikipedia")
        print(info)
        talk(info)    
    
    elif "who made you" in command or "who created you" in command or "who discovered you" in command:
            print("I was built by Mister Vishnu")
            talk("I was built by Mister Vishnu")
    
    
    elif 'for date' in command:   
        talk('sorry, I have a headache. Ask to Mister vishnu, he might come with you')
    
    elif 'are you single' in command:
        print("yes baby, just like you")
        talk("yes baby, just like you")
    
    
    elif 'joke' in command:
        #print(pyjokes.get_joke())
        talk(pyjokes.get_joke())
        
    elif 'news' in command:
        news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
        talk('Here are some headlines from the Times of India,Happy reading')
    
    elif "log off" in command or "sign out" in command:
            talk("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])
    
    elif 'ask' in command:
            talk('I can answer to computational and geographical questions and what question do you want to ask now')
            question = takecommand()
            app_id = "R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            print(answer)
            talk(answer)
    
    
    #elif " " in command:
    #    webbrowser.open_new_tab("https://youtu.be/xlOPqH8WUso")
        
         
while True:
    run_alexa()
