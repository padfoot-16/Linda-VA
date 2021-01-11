import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

engine=pyttsx3.init()
nasnes=sr.Recognizer()
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
command=None
def ahki(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    global command
    try:
        with sr.Microphone()  as mazder:
            print("hani nasma3...")
            sout = nasnes.listen(mazder)
            command=nasnes.recognize_google(sout)
            command=command.lower()
            if "linda" in command:
                command=command.replace("linda","")
                print(command)
                
    except:
        pass
    return command
def khaddem_linda(): 
    global command
    command=take_command()
    print(command)
    if "linda" in command:
        
        if 'play' in command:
            ghoneya=command.replace("play", "")
            ahki("playing" + ghoneya)
            print("playing" + ghoneya)
            pywhatkit.playonyt(ghoneya)
        elif  "time" in command:
            wakt=datetime.datetime.now().strftime("%I:%M %p,%A %B %d %Y")
            print(wakt)
            ahki("Current time is " + wakt) 
        elif "day" or "today"in command:
            lyoum=datetime.datetime.now().strftime("%A %B %d ")
            print("today is " + lyoum)
            ahki("today is " + lyoum)
        elif "date" in command:
            date=datetime.datetime.now().strftime("%A %B %d %Y") 
            ahki("the date is "+ date )       
        elif "who is " or "what is" in command:
            abd=command.replace("who is","")
            info=wikipedia.summary(abd,2)
            print(info)
            ahki(info)
        elif "date me" or "on a date" in command:
            print("fuck off")
            ahki("fuck off") 
        elif "who are you"  in command:
            print("i am a virtual assistant created by chiheb awini") 
            ahki("i am a virtual assistant created by cheeheb awini")
        elif "i want a girlfriend" or " i wanna a girlfriend" in command:
            print("Grow some balls and get one")
            ahki("Grow some balls and get one")       
    else:
        print(" My name is linda,Say again")
        ahki("My name is linda    ,    Say Again")      

while True:
    khaddem_linda()               