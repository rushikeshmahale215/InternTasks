import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests



recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "e5aeb28f353441b08db060b71c68116f"

def speak(text):
     engine.say(text)
     engine.runAndWait()
     
def aiProcess(command):
    import os

    from groq import Groq

    client = Groq(
           api_key="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"
            )


    chat_completion = client.chat.completions.create(
    messages=[
             {
                "role": "user",
                "content": command,
            }
                 ],
                model="llama-3.3-70b-versatile",
                 )

    return chat_completion.choices[0].message.content
     
def ProcessCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open instagram" in  c.lower():
        webbrowser.open("https://instagram.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
        
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        

        # Request the data
        # Parse and extract titles
        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])
            
            for article in articles:
                speak(article['title'])
                
    else:
        #Let OpenAi handle this request
        output = aiProcess(c)
        speak(output)

        
         
        
    

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        #Litsen for the wake word "Jarvis"
        # Obtain audio from microphone
        r = sr.Recognizer()
        
       
        print("recognizing...")
        # recognize speak using sphinx
        try:
            with sr.Microphone() as source:
              print("Listening...")
              audio = r.listen(source,timeout=2,phrase_time_limit=1)
            word = r.recognize_google(audio)
            
            if(word.lower() == "jarvis"):
                speak("Yes")
                #Listen for command
                with sr.Microphone() as source:
                    print("Jarvis is available...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                  
                    ProcessCommand(command)
                  
           
        except Exception as e:
            print("Sphinx error; {0}".format(e))
    
    
    
    