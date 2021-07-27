import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia 
import webbrowser
import os


#sapi5 is a windows API to take voice
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour > 4 and hour < 12:
        speak("Good Morning Srijan Sir")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon Srijan Sir")
    else:
        speak("Good Evening Srijan Sir")               

  

def takeCommand():
    #Takes microphone input from user and returns string output

    r = sr.Recognizer()
    #Recogniser class helps in recognising voice
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        #pause_threshold is seconds of non speaking audio before a phrase is considered complete
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio , language='en-in')
        print(f"User said {query}\n")

    except Exception as e:
        #print (e)
        print("Pardon Sir")
        return "None"

    return query




if __name__ == '__main__':
    wishMe()
    speak("Sir ,You are very smart and dashing!")
    speak("Praanaaam Mummy aur Papa")
    speak("Hi I am Siri. Please tell me how may I help you")  
    while True:
        query = takeCommand().lower()

        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query , sentences = 3)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open google' in query:
            webbrowser.open('https://www.google.com/')

        elif 'open codewithharry' in query:
            webbrowser.open('https://www.youtube.com/channel/UCeVMnSShP_Iviwkknt83cww')

        elif 'open free code camp' in query:
            webbrowser.open('https://www.youtube.com/channel/UC8butISFwT-Wl7EV0hUK0BQ')
        
        elif 'open stackoverflow' in query:
            webbrowser.open('https://stackoverflow.com/')

        elif 'open youtube' in query:
            webbrowser.open('https://www.youtube.com/')

        elif 'open inbox' in query:
            webbrowser.open('https://mail.google.com/mail/u/1/?ogbl#inbox')

        elif 'open college mail' in query:
            webbrowser.open('https://mail.google.com/mail/u/0/#inbox')

        elif 'open github' in query:
            webbrowser.open('https://github.com/SrijanShovit')
        
        elif 'open figma' in query:
            webbrowser.open('https://www.figma.com/files/recent?fuid=941669725110835730')
        
        elif 'open dhoni' in query:
            webbrowser.open('https://www.youtube.com/watch?v=vReIM3GVrCA')
        
        elif 'open song' in query:
            webbrowser.open('https://www.youtube.com/watch?v=vReIM3GVrCA')
        
        elif 'play music' in query:
            music_dir = 'D:\songs'
            songs = os.listdir(music_dir)
            print (songs)
            os.startfile(os.path.join(music_dir , songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print (f"Sir, the time is {strTime}")
            speak (f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "E:\\others\\VScode\\Code.exe"
            os.startfile(codePath)

        elif 'exit' in query:
            speak("Thank you for your time , Sir!")
            exit()
        