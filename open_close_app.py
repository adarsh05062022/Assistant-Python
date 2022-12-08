import os
import webbrowser


def openApps(command):
        
        if "code" in command:
            os.startfile("C:\\Users\\anmol\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
    
        elif "vlc" in command:
            os.startfile("C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe")
        
        elif "facebook" in command:
            webbrowser.open("facebook.com")            

        elif "instagram" in command:
            webbrowser.open("instagram.com")

        elif "skype" in command:
            os.system("start skype")
        
        elif "spotify" in command:
            os.system("start Spotify")
        
        elif "firefox" in command:
            os.system("start firefox")

        elif "word" in command:
            os.system("start  shell:appsfolder\Microsoft.Office.WINWORD.EXE.15")

        elif "powerpoint" in command:
             os.system("start  shell:appsfolder\Microsoft.Office.POWERPNT.EXE.15")

        elif "excel" in command:
            os.system("start  shell:appsfolder\Microsoft.Office.EXCEL.EXE.15")

        elif "chrome" in command:
            os.system("start chrome")

        elif "camera" in command:
            os.system("start explorer shell:appsfolder\Microsoft.WindowsCamera_8wekyb3d8bbwe!App")

        elif "calculator" in command:
            os.startfile("C:\\Windows\\System32\\calc.exe")
        
        elif "command" in command:
            os.system("start explorer shell:appsfolder\Microsoft.WindowsTerminal_8wekyb3d8bbwe!App")

        elif "recorder" in command:
             os.system("start explorer shell:appsfolder\Microsoft.WindowsSoundRecorder_8wekyb3d8bbwe!App")
        
        
      



def closeApps(command):
        
        if "code" in command:
            os.system("TASKKILL /f /im code.exe")
    
        elif "vlc" in command:
            os.system("TASKKILL /f /im vlc.exe")

        elif "facebook" in command:
            os.system("TASKKILL /f /im firefox.exe")

        elif "instagram" in command:
             os.system("TASKKILL /f /im firefox.exe")

        elif "twitter" in command:
             os.system("TASKKILL /f /im firefox.exe")
        
        elif "skype" in command:
            os.system("TASKKILL /f /im Skype.exe")

        elif "camera" in command:
            os.system("TASKKILL /f /im WindowsCamera.exe")
          
        elif "word" in command:
            os.system("TASKKILL /f /im WINWORD.EXE")

        elif "powerpoint" in command:
            os.system("TASKKILL /f /im POWERPNT.EXE")

        elif "excel" in command:
            os.system("TASKKILL /f /im EXCEL.EXE")

        elif "spotify" in command:
            os.system("TASKKILL /f /im Spotify.exe")

        elif "chrome" in command:
            os.system("TASKKILL /f /im chrome.exe")

        elif "firefox" in command:
            os.system("TASKKILL /f /im firefox.exe")

        elif "calculator" in command:
            os.system("TASKKILL /f /im CalculatorApp.exe")

        elif "voice recorder" in command:
            os.system("TASKKILL /f /im VoiceRecorder.exe")    
                
  
  
