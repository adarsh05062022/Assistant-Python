from ftplib import all_errors
from assistantui import Ui_ASSISTANTUI
from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
from bs4 import BeautifulSoup
import speech_recognition as sr
import pyttsx3
import webbrowser
import pywhatkit
import os
import random
import datetime
import pyjokes
import wikipedia as wiki
import pyautogui
import keyboard
from googletrans import Translator
import requests
from pywikihow import search_wikihow
import sys
from open_close_app import *
from speak_function import *

# import light 






class all_functions():
    
    def wishme():
       hour = int(datetime.datetime.now().hour)
       if hour>=0 and hour<12:
           speak("Good Morning")
       elif hour>=12 and hour<16:
           speak("Good Afternoon")        
       else:
           speak("Good Evening")
       speak("How can I assist you ?") 

    def youtube(command):
        
        if "open" in command:
            speak("What should I search on the youtube")        
            command = MainThread.TakeCommand("")
            speak("Ok,Sir")
            webbrowser.open("https://www.youtube.com/results?search_query="+command)
        elif "play" in command:
            song = command.replace("play","")  
            speak("playing.")
            pywhatkit.playonyt(song)
            # all_functions.Autoyoutube()
        else:
            speak("ok")
            pywhatkit.playonyt(command)   
    
    def wikipedia(command):
        command = command.replace("wikipedia","")
        command = command.replace("who is","") 
        try:
          summary = wiki.summary(command,sentences=2)
          speak(summary)
        except:   
            speak("Sorry,I am unable to get details")
    
    def joke():
        speak("here is a joke,")
        joke = pyjokes.get_joke()
        speak(joke)  

    def Temperature(command):
        try:
           url= f"https://www.google.com/search?q={command}"
           r = requests.get(url)
           data = BeautifulSoup(r.text,"html.parser")
           temp = data.find("div", attrs = {"class": "BNeawe"}).text
           str = (data.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text).split("\n")
           sky = str[1]
           speak(f"the Temperature is {temp} and wheather is {sky}")
        
        except:
            speak("Provide the correct location, I am unable to get details.")
    
         

class MainThread(QThread):    

    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.Execution() 

    def TakeCommand(self):
            listener=sr.Recognizer()   
            with sr.Microphone() as Source:
                print("\nListening......")
                listener.energy_threshold = 300
                listener.pause_threshold = 1.2        
                audio = listener.listen(Source)
            try:
               print("Recognizing.....")
               command = listener.recognize_google(audio,language="en-US")   
            #    command = input("Enter Input")                
               print(f"Your command :- {command}")
               return command.lower()  
            
            except Exception as Error:
                return "none"

             


        #------------------------Functions-------------------#
          
                   
    def Execution(self): 
        while True: 
            self.command = self.TakeCommand()
            
            if "hello" in self.command or "hey" in self.command:
                speak("Hello Sir, How can I help you?")

            elif 'youtube' in self.command:
               all_functions.youtube(self.command) 
            
            elif "wikipedia" in self.command:
               all_functions.wikipedia(self.command)
            
            elif 'open google' in self.command:                
                speak("what should I search Sir")
                query =self.TakeCommand()
                speak("Searching on google....")
                pywhatkit.search(query)

            elif "on google" in self.command or "search" in self.command:                
                command = self.command.replace("on google","")
                command = command.replace("google","")
                command = command.replace("search","")            
                speak("This is what I found on the web")
                try:
                    result  = wiki.summary(command,sentences=2)

                    speak(result)
                    # pywhatkit.search(command)
                except:
                    pywhatkit.search(command)   
            
            elif "who" in self.command or "when" in self.command or "where" in self.command:
                speak("This is what I found on the web")
                try:
                    result  = wiki.summary(self.command,sentences=2)
                    speak(result)
                    # pywhatkit.search(command)
                except:
                    pywhatkit.search(self.command)   
            
            elif "joke" in self.command or "jokes" in self.command:
               all_functions.joke() 
            
            elif "open" in self.command:
               speak("Ok sir")
               openApps(self.command)
            
            elif "close" in self.command:
               speak("Ok sir")
               closeApps(self.command)
                
            elif "how to" in self.command:
                speak("getting data from the internet.... ")
                max_result = 1
                how_to = search_wikihow(self.command,max_result)
                assert len(how_to) ==1
                speak(how_to[0].summary)
            
            elif "time" in self.command:
                strTime = datetime.datetime.now().strftime(" %H %M %S")                
                speak(f"Current time is :-{strTime}")
        
            elif "date" in self.command:
                strDate = datetime.datetime.now().date() 
                speak(f"Date is :- {strDate}") 

            elif 'temperature' in self.command or "weather" in self.command or "how is the day" in self.command:
            #    self.command = self.command.replace("how is the day","how is the weather") 
               all_functions.Temperature(self.command)
             
            elif "play music" in self.command or "song" in self.command or "play songs" in self.command:
                speak("playing.....")
                music_dir = "music"   
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,songs[random.randint(0,len(songs)-1)])) 

            elif "screenshot" in self.command or "capture" in self.command:
               try:
                 speak("Ok Boss , What should I name this ")
                 name = self.TakeCommand()
                 fullname = name + ".png"   
                 path = 'screenshot\\'+fullname             
                 var = pyautogui.screenshot()
                 var.save(path)  
                 os.startfile(path)

               except:
                 speak("failed to capture") 
 
            elif "about yourself" in self.command:
                speak("Hey, my name is not decided yet but you can call me anything you want. I'm made with the codes so you can easily change me . I'm something like you , Thank you for asking . It's a great experience to tell you about myself")

            elif "are you" in self.command:
                if "how" in self.command:
                    speak("I'm good. And I hope you are also good")    
                elif "single" in self.command:
                    speak("sorry I am in relationship with your computer")
             
            elif "bye" in self.command or "quit" in self.command or "you need to stop" in self.command or "goodbye" in self.command or "i am going" in self.command or "i will call you later" in self.command:
                speak("Bye sir, It's nice talk with you")                
                break
      
      # when arduino is connected

            # elif "turn on" in self.command:
            #     val = light.turnon(self.command)
            #     speak(val)

            # elif "turn off" in self.command:
            #     val = light.turnoff(self.command)
            #     speak(val)                


 

startFunction = MainThread()         

class Gui_start(QMainWindow):

    def __init__(self):
        super().__init__()
        self.assistant_ui = Ui_ASSISTANTUI()
        self.assistant_ui.setupUi(self)
        self.assistant_ui.movies_label = QtGui.QMovie("GUI_IMAGES\Simple Black and White Text Gif.gif")
        self.assistant_ui.label.setMovie(self.assistant_ui.movies_label)
        self.assistant_ui.movies_label.start()

        self.assistant_ui.movies_label_3 = QtGui.QMovie("GUI_IMAGES\Title.jpg")
        self.assistant_ui.label_3.setMovie(self.assistant_ui.movies_label_3)
        self.assistant_ui.movies_label_3.start()

        self.assistant_ui.movies_label_4 = QtGui.QMovie("GUI_IMAGES\TEAM -MEMBER.jpg")
        self.assistant_ui.label_4.setMovie(self.assistant_ui.movies_label_4)
        self.assistant_ui.movies_label_4.start()


        self.assistant_ui.pushButton.clicked.connect(self.startFunc)
        self.assistant_ui.pushButton_2.clicked.connect(self.close)
        
    
    def startFunc(self):     
        all_functions.wishme()
        startFunction.start()
        

        

Gui_App = QApplication(sys.argv)  
Gui_assistant = Gui_start()     
Gui_assistant.show()
exit(Gui_App.exec_())
          
                
       

    
    
    
    