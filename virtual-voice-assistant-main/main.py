import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import requests
import pywhatkit
import pyjokes
from tkinter import *
from tkinter import messagebox
import keyboard
from PIL import ImageTk, Image
import pymysql



name_file = open("Assistant_name", "r")
name_assistant = name_file.read()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    print(name_assistant + " : " + text)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if (hour >= 0) and (hour < 12):
        speak("Hello, Good Morning")
    elif (hour >= 12) and (hour < 18):
        speak("Hello, Good Afternoon")
    else:
        speak("Hello, Good Evening")

# def askname():
#     speak("What is your name dear?")
#     name = takeCommand()
#     speak("Welcome " + name)

def takeCommand():
    r = sr.Recognizer()
    # t= Translator()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source, timeout=100, phrase_time_limit=5)

        try:
            print("Recognizing...")
            statement = r.recognize_google(audio,language='en-in')
            print(f"User said:{statement}\n")

        except Exception as e:
            print('Unable to Recognize your voice.')
            speak("Unable to Recognize your voice.")
            return "None"
        return statement


def Process_audio():
    run = 1
    while run == 1:
        speak("Hi, I'm your personal assistant - " + name_assistant)
        wishMe()
        speak("How can I help you?")
        run += 1

    if __name__ == '__main__':

        while True:
            
            statement = takeCommand().lower()

            if "goodbye" in statement or "bye" in statement or "stop" in statement or 'exit' in statement:
                speak('Your personal assistant ' + name_assistant + ' is shutting down, Good bye')
                screen.destroy()
                break
            
            # elif "Speak in hindi" in statement:
            #     speak_hindi()

            elif 'open youtube' in statement:
                webbrowser.open_new_tab("https://www.youtube.com")
                speak("youtube is open now")
                time.sleep(10)

            elif 'open google' in statement:
                webbrowser.open_new_tab("https://www.google.com")
                speak("Google chrome is open now")
                time.sleep(10)

            elif 'open gmail' in statement:
                webbrowser.open_new_tab("https://www.gmail.com")
                speak("Google Mail open now")
                time.sleep(10)

            elif "open notepad" in statement:
                speak("Opening notepad")
                path = "c:\\windows\\system32\\notepad.exe"
                os.startfile(path)
                time.sleep(10)

            elif "close notepad" in statement:
                speak("Closing notepad")
                os.system("TASKKILL /F /IM notepad.exe") 

            elif "open calculator" in statement:  # -----------> Working fine but once opened it not gets closed by voice command
                speak("Opening calculator")
                path = "c:\\windows\\system32\\calc.exe"
                os.startfile(path)
                time.sleep(5)

            elif "open chrome" in statement:
                speak("Opening chrome")
                path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
                os.startfile(path)
                time.sleep(10)

            elif "close chrome" in statement:
                speak("Closing chrome")
                os.system("TASKKILL /F /IM chrome.exe")

            elif "weather" in statement:
                api_key = "8ef61edcf1c576d65d836254e11ea420"
                base_url = "https://api.openweathermap.org/data/2.5/weather?"
                speak("whats the city name")
                city_name = takeCommand()
                complete_url = base_url+"appid="+api_key+"&q="+city_name
                response = requests.get(complete_url)
                x = response.json()
                if x["cod"] != "404":
                    y = x["main"]
                    current_temperature = y["temp"]
                    current_humidiy = y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]
                    speak(" Temperature in kelvin unit = " + str(current_temperature) + "\n humidity (in percentage) = " + str(current_humidiy) + "\n description = " + str(weather_description))

                else:
                    speak(" City Not Found ")
            
            elif 'play' in statement:
                song = statement.replace('play', '')
                speak('playing' + song)
                pywhatkit.playonyt(song)
                time.sleep(10)

            elif "song" in statement:
                speak("Which song will you like to hear")

            elif 'how are you' in statement:
                speak("I am fine, Thank you")
                speak("How are you")
    
            elif 'fine' in statement or "good" in statement:
                speak("It's good to know that your fine")

            elif 'good morning' in statement:
                speak("A very good morning dear")

            elif 'good afternoon' in statement:
                speak("Good afternoon dear")

            elif 'good night' in statement:
                speak("A very good night dear, sweet dreams")

            elif 'robot' in statement:
                speak("I don't have any robotic parts - I'm software that runs on your phone and desktops")

            elif "where is" in statement:
                statement = statement.replace("where is", "")
                location = statement
                speak("User asked to Locate")
                speak(location)
                webbrowser.open("https://www.google.com/maps/place/" + location + "")

            elif 'time' in statement:
                strTime = datetime.datetime.now().strftime("%I:%M %p")
                speak(f"The time is {strTime}")

            elif 'who are you' in statement or 'what can you do' in statement:
                speak('I am ' + name_assistant + 'version 1 point O your personal assistant. I am programmed to minor tasks like'
                    'opening youtube, google chrome, gmail and stackoverflow, predict time, take a photo, search wikipedia, predict weather' 
                    'in different cities, get top headline news from times of india and you can ask me computational or geographical questions too!')


            elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement or "who is your creator" in statement:
                speak("I was built by Aditya, Vishnu And Prachiti")

            elif 'for date' in statement:   
                speak('Sorry, I have a headache. Ask to Siri, she might come with you')
        
            elif 'are you single' in statement:
                speak("yes baby, just like you")

            elif 'i love you' in statement:
                speak("Sorry, I'm in relationship with Siri")

            elif "open stackoverflow" in statement:
                webbrowser.open_new_tab("https://stackoverflow.com/login")
                speak("Here is stackoverflow")
                time.sleep(10)

            elif 'news' in statement:
                news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
                speak('Here are some headlines from the Times of India,Happy reading')
                time.sleep(6)

            elif "camera" in statement or "take a photo" in statement:
                ec.capture(0,"robo camera","img.jpg")

            elif 'search' in statement:
                statement = statement.replace("search", "")
                webbrowser.open_new_tab(statement)
                time.sleep(5)

            elif 'joke' in statement or 'entertain' in statement:
                print("Here is a joke for you :")
                joke = pyjokes.get_joke()
                speak(joke)
                time.sleep(5)

            elif 'ask' in statement:
                speak('Yes, I can answer to computational and geographical questions and what question do you want to ask now')
                question = takeCommand()
                app_id = "R2K75H-7ELALHR35X"
                client = wolframalpha.Client('R2K75H-7ELALHR35X')
                res = client.query(question)
                answer = next(res.results).text
                speak(answer)

            elif 'wikipedia' in statement or 'who is' in statement:
                speak('Searching Wikipedia...')
                statement = statement.replace("wikipedia", "")
                results = wikipedia.summary(statement, sentences=3)
                speak("According to Wikipedia")
                speak(results)

            elif "log off" in statement or "sign out" in statement:
                speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
                subprocess.call(["shutdown", "/l"])

            elif 'shutdown' in statement:
                speak("Hold on a sec! Your system is on its way to shutdown")
                subprocess.call(["shutdown", "/s"])

            elif 'restart' in statement:
                speak("Your system will restart now")
                subprocess.call(["shutdown", "/r"])

            elif "bored" in statement:
                speak("I'm here to do cool tasks for you")
                speak("What should I do")
                speak("Should I play a song or tell you a joke")

            elif 'what are you doing' in statement:
                speak("Nothing dear, I'm here to help you.")
                speak("Tell me what should I do for you")

            elif 'hello' in statement:
                speak("Hello dear, have a good day")

            elif 'thank you' in statement:
                speak("I'm honoured to serve")

            elif 'what is your name' in statement:
                speak('Well, my name is ' + name_assistant + ', I wish everyone have a good name as mine')

            elif "don't listen" in statement or "stop listening" in statement:
                speak("for how much time you want to stop me from listening commands")
                a = int(takeCommand())
                time.sleep(a)
                print(a)

            elif "write a note" in statement:
                speak("What should i write, sir")
                note = takeCommand()
                file = open('note.txt', 'w')
                speak("Sir, Should i include date and time")
                snfm = takeCommand()
                if 'yes' in snfm or 'sure' in snfm:
                    strTime = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                    file.write(strTime)
                    file.write(" :- ")
                    file.write(note)
                    speak("Note was successfully created")
                else:
                    file.write(note)

            else:
                speak("Please say it again")


def change_name():

  name_info = name.get()

  file=open("Assistant_name", "w")

  file.write(name_info)

  file.close()

  settings_screen.destroy()

  screen.destroy()

def change_name_window():
    
    global settings_screen
    global name

    settings_screen = Toplevel(screen)
    settings_screen.title("Settings")
    settings_screen.geometry("500x500+700+200")
    settings_screen.iconbitmap('app_icon.ico')

      
    name = StringVar()

    current_label = Label(settings_screen, text = "Current name: " + name_assistant)
    current_label.pack()

    enter_label = Label(settings_screen, text = "Please enter your Virtual Assistant's name below")
    enter_label.pack(pady=10)
      

    Name_label = Label(settings_screen, text = "Name")
    Name_label.pack(pady=10)
     
    name_entry = Entry(settings_screen, textvariable = name)
    name_entry.pack()


    change_name_button = Button(settings_screen, text = "Ok", width = 10, height = 1, command = change_name)
    change_name_button.pack(pady=10)

def info():

    info_screen = Toplevel(screen)
    info_screen.title("Info")
    info_screen.iconbitmap('app_icon.ico')
    info_screen.geometry("600x200+650+350")

    creator_label = Label(info_screen, text="Created by Vishnu Yelde and Aditya Sharma. Prachiti Yadav helped in cooperating")
    creator_label.pack(pady=10)

    for_label = Label(info_screen, text="For Python mini project")
    for_label.pack()

    keyboard.add_hotkey("F4", Process_audio)
    
def exit():
    screen.destroy()

def wikipedia_screen(text):
    wikipedia_screen = Toplevel(screen)
    wikipedia_screen.title(text)
    wikipedia_screen.iconbitmap('app_icon.ico')

    message = Message(wikipedia_screen, text=text)
    message.pack()

# ---------------------------------- Connect to Database ----------------------------------

def connect_database():
    if username_entry.get() == '' or password_entry.get() == '':
        messagebox.showerror('Error', 'All fields are required')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='Vishnu@2525')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', "Database connectivity issue")
            return

        try:
            query = 'create database userdata'
            mycursor.execute(query)
            query = 'use userdata'
            mycursor.execute(query)
            query = 'create table data(id int auto_increment primary key not null, username varchar(100), password varchar(30))'
            mycursor.execute(query)
        except:
            mycursor.execute('use userdata')

        query = 'select * from data where username=%s'
        mycursor.execute(query, (username_entry.get()))

        row = mycursor.fetchone()
        if row != None:
            messagebox.showerror('Error', 'Username already exists!')
        else:
            query = 'insert into data(username, password) values(%s,%s)'
            mycursor.execute(query, (username_entry.get(), password_entry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success', 'Registered successfully')
            clear()
            signup_screen.destroy()
            login()

def clear():
    username_entry.delete(0,END)
    password_entry.delete(0,END)


# ------------------------------ Check credentials -----------------------------

def login_user():
    if username_entry.get() == '' or password_entry.get() == '':
        messagebox.showerror('Error', 'All Fields are required')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='Vishnu@2525')
            mycursor = con.cursor()
        except Exception as e:
            messagebox.showerror('Error', "Database connectivity issue")
            print(e)
            return
        query = 'use userdata'
        mycursor.execute(query)
        query = 'select * from data where username=%s and password=%s'
        mycursor.execute(query, (username_entry.get(), password_entry.get()))
        row = mycursor.fetchone()
        if row == None:
            messagebox.showerror('Error', 'Invalid username or password')
        else:
            messagebox.showinfo('Welcome', 'Logged in successfully')
            switch_to_main_screen()

# --------------------------------- Signup page start ---------------------------------------

def signup():
    global signup_screen

    signup_screen = Tk()
    signup_screen.title("Signup Page - Virtual Voice Assistant - " + name_assistant)
    signup_screen.geometry('990x660+450+180')
    signup_screen.configure(bg='white')
    bgImage1 = ImageTk.PhotoImage(file='background.png')
    bgLabel = Label(signup_screen, image=bgImage1, bd=0)
    bgLabel.place(x=70, y=150)

    heading = Label(signup_screen, text="CREATE AN ACCOUNT", font=("Microsoft YAHei UI Light", 20, 'bold'), bg='white', fg='#57a1f8')
    heading.place(x=550, y=100)

    global username_entry
    username_entry = Entry(signup_screen, width=30, font=("Microsoft YAHei UI Light", 12, 'bold'), bd=0, fg='#555555')
    username_entry.place(x=550, y=200)
    username_entry.insert(0, 'Username')
    username_entry.bind('<FocusIn>', user_enter)

    frame1 = Frame(signup_screen, width=350, height=2, bg='#555555')
    frame1.place(x=550, y=230)

    global password_entry
    password_entry = Entry(signup_screen, width=30, font=("Microsoft YAHei UI Light", 12, 'bold'), bd=0, fg='#555555')
    password_entry.place(x=550, y=270)
    password_entry.insert(0, 'Password')
    password_entry.bind('<FocusIn>', pass_enter)

    frame2 = Frame(signup_screen, width=350, height=2, bg='#555555')
    frame2.place(x=550, y=300)

    create_acc_button = Button(signup_screen, text="Create account", width=25, font=('Open Sans', 14, 'bold'), fg='white', bg='#57a1f8', activeforeground='white', activebackground='#57a1f8', cursor='hand2', bd=0, command=connect_database)
    create_acc_button.place(x=550, y=350)

    or_label = Label(signup_screen, text='---------------------- OR ----------------------', font=('Open Sans', 12), fg="#555555", bg='white')
    or_label.place(x=550, y=430)

    login_label = Label(signup_screen, text="Already have an account?", font=('Open Sans', 12, 'bold'), fg="#555555", bg='white')
    login_label.place(x=550, y=480)

    already_acc_button = Button(signup_screen, text="Login here", font=('Open Sans', 12, 'bold underline'), fg='#57a1f8', bg='white', activeforeground='white', activebackground='white', cursor='hand2', bd=0, command=login_page)
    already_acc_button.place(x=800, y=475)

    signup_screen.mainloop()


def signup_page():
    login_screen.destroy()
    signup()

# --------------------------------- Signup page end ---------------------------------------

# --------------------------------- Login page start ---------------------------------------

def user_enter(event):
    if username_entry.get() == 'Username':
        username_entry.delete(0, END)

def pass_enter(event):
    if password_entry.get() == 'Password':
        password_entry.delete(0, END)

def login():
    global login_screen

    login_screen = Tk()
    login_screen.title("Login Page - Virtual Voice Assistant - " + name_assistant)
    login_screen.geometry('990x660+450+180')
    login_screen.configure(bg='white')
    login_screen.resizable(False, False)
    bgImage = ImageTk.PhotoImage(file='background.png')
    bgLabel = Label(login_screen, image=bgImage, bd=0)
    bgLabel.place(x=70, y=150)

    heading = Label(login_screen, text="USER LOGIN", font=("Microsoft YAHei UI Light", 23, 'bold'), bg='white', fg='#57a1f8')
    heading.place(x=595, y=100)

    global username_entry
    username_entry = Entry(login_screen, width=25, font=("Microsoft YAHei UI Light", 12, 'bold'), bd=0, fg='#555555')
    username_entry.place(x=575, y=200)
    username_entry.insert(0, 'Username')
    username_entry.bind('<FocusIn>', user_enter)

    frame1 = Frame(login_screen, width=300, height=2, bg='#555555')
    frame1.place(x=575, y=230)

    global password_entry
    password_entry = Entry(login_screen, width=25, font=("Microsoft YAHei UI Light", 12, 'bold'), bd=0, fg='#555555')
    password_entry.place(x=575, y=270)
    password_entry.insert(0, 'Password')
    password_entry.bind('<FocusIn>', pass_enter)

    frame2 = Frame(login_screen, width=300, height=2, bg='#555555')
    frame2.place(x=575, y=300)

    login_button = Button(login_screen, text="Login", width=21, font=('Open Sans', 14, 'bold'), fg='white', bg='#57a1f8', activeforeground='white', activebackground='#57a1f8', cursor='hand2', bd=0, command=login_user)
    login_button.place(x=575, y=340)

    or_label = Label(login_screen, text='---------------- OR ----------------', font=('Open Sans', 14), fg="#555555", bg='white')
    or_label.place(x=575, y=420)

    signup_label = Label(login_screen, text="Don't have an account?", font=('Open Sans', 11, 'bold'), fg="#555555", bg='white')
    signup_label.place(x=580, y=480)

    new_acc_button = Button(login_screen, text="Sign Up", font=('Open Sans', 11, 'bold underline'), fg='#57a1f8', bg='white', activeforeground='white', activebackground='white', cursor='hand2', bd=0, command=signup_page)
    new_acc_button.place(x=800, y=475)

    login_screen.mainloop()

def login_page():
    signup_screen.destroy()
    login()

    # ---------------------------- Login page end ---------------------------

def switch_to_main_screen():
    login_screen.destroy()
    main_screen()

def main_screen():

    global screen
    screen = Tk()
    screen.title("Virtual Voice Assistant - " + name_assistant)
    screen.geometry("1100x750+400+100")
    screen.iconbitmap('app_icon.ico')

    frame = Frame(screen, width=50, height=25)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)

    img = ImageTk.PhotoImage(Image.open("assistant.jpg"))
    label = Label(frame, image=img)
    label.pack()

    showCommand = StringVar()
    cmdLabel = Label(screen, textvariable=showCommand, bg='LightBlue1',
                     fg='black', font=('Courier', 15))
    cmdLabel.place(x=250, y=150)

    name_label = Label(text=name_assistant, font=("Calibri", 30))
    name_label.place(x=500, y=530)

    microphone_photo = PhotoImage(file="microphone.png")
    microphone_button = Button(image=microphone_photo, command=Process_audio)
    microphone_button.place(x=475, y=665)

    settings_photo = PhotoImage(file="settings.png")
    settings_button = Button(image=settings_photo, command=change_name_window)
    settings_button.place(x=375, y=665)
        
    info_photo = PhotoImage(file="info.png")
    info_button = Button(image=info_photo, command=info, font = ("Calibri", 15))
    info_button.place(x=575, y=665)
    
    # exit_button
    exit_button = Button(text="Exit", command=exit, font = ("Calibri", 20))
    exit_button.place(x=670, y=665)

    screen.mainloop()


# main_screen()
login()
