import pyttsx3
import speech_recognition as sr
import datetime
import os
import webbrowser

engine = pyttsx3.init('sapi5') #speech programing  apllication for window
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(audiovoice):
    print(audiovoice)
    engine.say(audiovoice)
    engine.runAndWait()

def greet():
    hour = int(datetime.datetime.now().hour)
    print(hour)
    if hour>=0 and hour<11:
        speak('Good Morning')
    elif hour>=11 and hour<15:
        speak('Good Afternoon')
    elif hour>=15 and hour<24:
        speak('Good Evening')
    speak('I am your Personal Assistant')

def askname():
    speak('What is your name?')
    name=takevoicecommand()
    speak('Welcome' +name)
    speak('How can I help you')
def takevoicecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        try:
            audio=r.listen(source,timeout=30,phrase_time_limit=10)
            print("Compiling your voice please wait..")
            text=r.recognize_google(audio,language="en-in")
            print(text)
        except Exception as e:
            speak('Unable to recognize your voice')
        return text


if __name__=='__main__':
    greet()
    askname()
    while True:
        work=takevoicecommand().lower()
        if 'how are you' in work:
            speak('I am fine. Thank You')
            speak('How are you?')
        elif 'fine' in work or 'good' in work:
            speak('Its good to know that you are fine')
        elif 'open notepad' in work:
            path="C:\\Windows\\notepad.exe"
            os.startfile(path)
        elif 'close notepad' in work:
            os.system("TASKKILL /F /IM notepad.exe")
        elif 'open chrome' in work:
            url="www.google.com"
            chrome_path='C:/Users/HP/AppData/Local/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)
        elif 'close chrome' in work:
            os.system("TASKKILL /F /IM chrome.exe")
        elif 'open youtube' in work:
            url1="www.youtube.com"
            chrome_path='C:/Users/HP/AppData/Local/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url1)
        elif 'close youtube' in work:
            os.system("TASKKILL /F /IM chrome.exe")
        elif 'open hackerrank' in work:
            url2="www.hackerrank.com"
            chrome_path='C:/Users/HP/AppData/Local/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url2)
        elif 'close hackerrank' in work:
            os.system("TASKKILL /F /IM chrome.exe")

        elif 'open leetcode' in work:
            url3="www.leetcode.com"
            chrome_path='C:/Users/HP/AppData/Local/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url3)
        elif 'close leetcode' in work:
            os.system("TASKKILL /F /IM chrome.exe")
        elif 'bye' in work:
            speak('bye.. see you again')
            exit()
        else:
            speak('I cant understand please speak again')