import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibary


recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()  

def processCommand(c):
   if "open google" in c.lower():
        webbrowser.open("https://google.com")
   elif  "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
   elif  "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
   elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
   elif c.lower().startswith("play"):
       song = c.lower().split(" ")[1]
       link = musicLibary.music[song]
       webbrowser.open(link)

       
if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)
            command = recognizer.recognize_google(audio)
            if command.lower() == "jarvis":
                speak("Ya")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    processCommand(command)
        except Exception as e:
            print("Error; {0}".format(e))
            
