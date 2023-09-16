#jarvis  Codebrokerrose/jarvis_the_voice_assistant
import pyttsx3 #module to speech conversion library in python (pip install pyttsx3)
import speech_recognition as sr #pip install speech recognization(also pip install play audio)
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
from googlesearch import * #pip install google
import webbrowser
import requests #pip install requests
from bs4 import BeautifulSoup #pip install googlesearch-python beautifulsoup4


#iexplorer_path = r'C:\Program Files (x86)\Internet Explorer\iexplore.exe %s'
chrome_path = r"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
#init function to get an engine instance for the speech synthesis
engine = pyttsx3.init('sapi5') #use to take voices inbuild property
voices = engine.getProperty('voices') #getting details of current voice
# print(voices[1].id) #1 for girl 0 for boy voice
engine.setProperty('voice',voices[1].id) #set voice proprty of engine

def speak(audio):#whatever argument this will take,this will speak it
    engine.say(audio) #whatever audio is fed then engine will speak it ie.say method on the engine that passing input text to be spoken 
    engine.runAndWait() #run and wait method , it proceses the voice command

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=4 and hour<12:
        speak("GOOD MOORNING!")
    elif hour>=12 and hour<18:
        speak("GOOD AFTERNOON!")
    elif hour>=18 and hour<21:
        speak("GOOD EVENING!")
    speak("Hi master i am Jarvis. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

# def takeCommand():
#     #it takes microphone input from the user and returns string output
#     r = sr.Recognizer()
#     with sr.Microphone() as source: #i will use this as source microphone
#         print("Listening...") #it should be known that the program is being used
#         r.pause_threshold = 1
#         audio = r.listen(source)
#     try:
#         print("Recognizing...")
#         query = r.recognize_google(audio, Language='en-in') #recognize google,google cloud and many things are available
#         print("User said: ",query)  
#     #we are recognising the audio here whatever audio is typed

#     except sr.RequestError as e :
#         # print(e)
#         print("Say that again please")
#         return "None"
#     return query
def sendEmail(to, content):#enable less secure apps
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

# Perform the Google search and get the results
def perform_google_search(query):
    try:
        results = list(search(query, num=2, stop=2, pause=2.0))  # You can adjust the number of results and pause time
        return results
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return []

# Function to extract the first two sentences from a webpage
def extract_first_two_sentences(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        
        # Combine the text of the first two paragraphs
        text = ''.join([p.text for p in paragraphs[:2]])
        
        # Split the text into sentences and return the first two
        sentences = text.split('.')
        return '. '.join(sentences[:2])
    except Exception as e:
        print(f"An error occurred while extracting text: {str(e)}")
        return ""

if __name__ =="__main__": #__name__ is the buid in variable which evaluates to the name of the current module.
    wishMe()
    # speak("well done girl good going. keep it up")
    # takeCommand()
    while True:
    # if 1:
        query = takeCommand().lower()#Converting user query into lower case
        #logic for executing tasks on query
        if 'wikipedia' in query: #if wikipedia found in the query then this block will be executed
            speak('Searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2) #return 2sentense from wikipedia
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open("youtube.com")
        elif 'open whatsapp' in query:
            webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open("web.whatsapp.com")
        elif 'open google' in query:
            speak('Opening google..')
            webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open("google.com")
        elif 'open instagram' in query:
            webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open("instagram.com")
        elif 'open facebook' in query:
            webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open("facebook.com")
        elif 'open twitter' in query:
            webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open("twitter.com")
        elif 'open stackoverflow' in query:
            webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open("stackoverflow.com")
        elif 'open chat gpt' in query:
            webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open("chat.openai.com")
        elif 'play music' in query:
            music_dir ='C:\\Users\\Windows 10\\Music'
            songs = os.listdir(music_dir) #list all the files in music dir 
            print(songs)
            os.startfile(os.path.join(music_dir ,songs[0]))
        elif 'open xammp' in query:
            path="C:\\xampp\\xampp-control.exe"
            os.startfile(path)
        elif 'open git bash' in query:
            path="C:\\Program Files\\Git\\git-bash.exe" 
            os.startfile(path)
        elif 'the time' in query: #whats the time jurvis
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Master the time is {strTime}") 
        elif 'open code' in query:
            codePath ="C:\\Users\\Windows 10\\Desktop\\Java\\SukanyaSaha\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        #make dictionary attacth all email id
        elif 'send email' in query:
            try:
                speak("What should i say?")
                content = takeCommand() #whatever i say convert it into string
                to = "yourownemail@gmail.com"
                sendEmail(to, content)
                speak("Email has been send!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email") 
        elif 'open google' in query:
            
            webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open("https://google.com")
        elif 'exit' in query:
            speak('Goodbye Master!')
            exit(); 
        else:
            try:
                from googlesearch import search 
            except ImportError:
                print("No module named 'google' found")
            #to search
            for j in search(query, tld="co.in", num=10 ,stop=10, pause=2):
                print(j) 
            # Call the function and print the first two sentences from the search results
            search_results = perform_google_search(query)
            for i, result in enumerate(search_results, start=1):
                print(f"Result {i}: {result}")
                first_two_sentences = extract_first_two_sentences(result)
                print(f"{first_two_sentences}\n")
                speak(f"{first_two_sentences}\n")
            
            for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
                webbrowser.open("https://google.com/search?q=%s" % query)
