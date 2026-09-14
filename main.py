import speech_recognition as sr 
import webbrowser   
import pyttsx3  
import musicLibrary 
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "7b7aafa8f2374c7e8822206fb1a1f39e"
def speak(text):
    engine.say(text)
    engine.runAndWait()


def processCommand(c):
    if  "open google" in c.lower():
         webbrowser.open("https://www.google.com")
    elif"open youtube" in c.lower():
         webbrowser.open("https://www.youtube.com") 
    elif "open facebook" in c.lower():
         webbrowser.open("https://www.facebook.com")
    elif "open instagram" in c.lower():
         webbrowser.open("https://www.instagram.com")
    elif "open twitter" in c.lower():
         webbrowser.open("https://www.twitter.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link =musicLibrary.music[song]
        webbrowser.open(link) 

'''    elif "news" in c.lower():
         r.requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")   
         if r.status_code == 20:
            data = r.json()
            articles = data.get("articles",[])
            for article in articles:
                speak(article["title"])'''
            
         
         
         


    
if __name__ == "__main__":
    speak("initializing jarvis.........") 
    while True:
        # listen for the jarvis wake word 
        # obtain audio from the microphone 

        r = sr.Recognizer()
           

        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("listening ...")
                audio = r.listen(source,timeout =5,phrase_time_limit=3)
            word = r.recognize_google(audio)
            if(word.lower()) == "jarvis": 
                        speak("Yes sir, how can I help you?")
                    # listen for the next command 
            with sr.Microphone() as source:
                print("jarvis activated.....")
                audio = r.listen(source)
                word = r.recognize_google(audio)
                processCommand(word)
                       
                    
                            
        except Exception as e:
            print("; {0}".format(e))
