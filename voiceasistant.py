import pyttsx3
import os
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import wikipedia
import random
print("#####################################  WELCOME  ##########################################")
#pyttsx3.speak("welcome to your personal voice assistant ")
print()

while True:
    x = print("what you want me to do")

    r = sr.Recognizer()  
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("start say..")
        audio = r.record(source, duration= 5)
        print("speech done ..")
        p = r.recognize_google(audio, language= 'en-in')
    if("Chrome" in p) and (("run" in p) or ("open" in p)):
        if "dont"in p:
           pyttsx3.speak("okk,as you say")
           pass
        else:
           pyttsx3.speak("Chrome will open in a second")
           os.system("start chrome")
           continue

    elif 'wikipedia' in p: 
            pyttsx3.speak('Searching Wikipedia...') 
            p = p.replace("wikipedia", "") 
            results = wikipedia.summary(p, sentences = 3) 
            pyttsx3.speak("According to Wikipedia") 
            print(results) 
            pyttsx3.speak(results) 
  
    elif("Chrome" in p)and("close"in p):
        pyttsx3.speak("closing chrome")
        os.system("taskkill/im chrome.exe")
    
    #elif "Wikipedia" in p:
        #webbrowser.open("www.wikipedia.com")

    elif "YouTube" in p:
        webbrowser.open("www.youtube.com")

    elif "Facebook" in p:
        webbrowser.open("www.facebook.com")

    elif 'joke' in p: 
        pyttsx3.speak(pyjokes.get_joke())
    
    elif("spotify" in p) and (("run" in p) or ("open" in p)):
        if "dont"in p:
           pyttsx3.speak("okk,as you say")
           pass
        else:
           pyttsx3.speak("spotify will open in a second")
           os.system(random.choice("start spotify"))
           continue
    elif("spotify" in p) and ("close"in p):
        pyttsx3.speak("closing spotify")
        os.system("taskkill/im spotify.exe")
    
    elif("Notepad" in p) and (("run" in p) or ("open" in p)):
        if "dont"in p:
           pyttsx3.speak("okk,as you say")
           pass
        else:
           pyttsx3.speak("Notepad will open in a second")
           os.system("start notepad")
           continue
    elif("Notepad" in p) and ("close"in p):
        pyttsx3.speak("closing Notepad")
        os.system("taskkill/im notepad.exe")
    elif("window Media" in p) and (("run" in p) or ("open" in p)):
        if "dont"in p:
           pyttsx3.speak("okk,as you say")
           pass
        else:
           pyttsx3.speak("window Media player will open in a second")
           os.system("start wmplayer")
           continue
    elif ("window Media" in p) and ("close"in p):
        pyttsx3.speak("closing window Media player")
        os.system("taskkill/im wmplayer.exe")
    elif("calculator" in p) and (("open" in p) or ("run" in p)):
        if "dont"in p:
           pyttsx3.speak("okk,as you say")
           pass
        else:
           pyttsx3.speak("calculator will open in a second")
           os.system("start calc")
           continue
    elif ("calculator" in p) and ("close"in p):
        pyttsx3.speak("closing calculator")
        os.system("taskkill/im calculator.exe")
    elif("my computer" in p) and (("open" in p) or ("run" in p)):
        if "dont"in p:
           pyttsx3.speak("okk,as you say")
           pass
        else:
           pyttsx3.speak("my computer will open in a second")
           os.system("start explorer")
           continue
    elif ("mycomputer" in p) and ("close"in p):
        pyttsx3.speak("access denied to close")
    elif("VLC" in p) and (("run" in p) or ("open" in p)):
        if "dont"in p:
           pyttsx3.speak("okk,as you say")
           pass
        else:
           pyttsx3.speak("vlc media player will open in a second")
           os.system("start vlc")
           continue
    elif ("VLC" in p) and ("close"in p):
        pyttsx3.speak("closing vlc media player")
        os.system("taskkill/im vlc.exe")

    elif("virtual Machine"in p ) and (("run" in p) or ("open" in p)):
        if "dont"in p:
           pyttsx3.speak("okk,as you say")
           pass
        else:
           pyttsx3.speak("virtual machine will open in a second")
           os.system("start virtualbox")
           continue
    elif ("virtual Machine" in p) and ("close"in p):
        pyttsx3.speak("closing virtual machine")
        os.system("taskkill/im virtualbox.exe")

    elif("MS paint" in p or "paint" in p) and (("run" in p) or ("open" in p)):
        if "dont"in p:
           pyttsx3.speak("okk,as you say")
           pass
        else:
           pyttsx3.speak("paint will open in a second")
           os.system("start mspaint")
           continue
    elif ("MS paint" in p or "paint" in p) and ("close"in p):
        pyttsx3.speak("closing paint")
        os.system("taskkill/im mspaint.exe")

    elif("task manager"in p) and (("run" in p) or ("open" in p)):
        if "dont"in p:
           pyttsx3.speak("okk,as you say")
           pass
        else:
           pyttsx3.speak("task manager will open in a second")
           os.system("start taskmgr")
           continue
    elif ("task manager" in p) and ("close"in p):
        pyttsx3.speak(" access denied to close")

    elif("calendar" in p) and (("run" in p) or ("open" in p)):
        if "dont"in p:
           pyttsx3.speak("okk,as you say")
           pass
        else:
           pyttsx3.speak("calendar will open in a second")
           os.system("start outlookcal:")
           continue
    elif ("calendar" in p) and ("close"in p):
        pyttsx3.speak(" access denied to close")

    elif ("clock" in p) and (("run" in p) or ("open" in p)):
        if "dont" in p:
            pyttsx3.speak("okk,as you say")
            pass
        else:
            pyttsx3.speak("clock will open in a second")
            os.system("start ms-clock:")
            continue
    elif ("clock" in p) and ("close"in p):
        pyttsx3.speak(" closing clock")
        os.system("taskkill/im time.exe")

    elif ("camera" in p) and (("run" in p) or ("open" in p)):
        if "dont" in p:
            pyttsx3.speak("okk,as you say")
            pass
        else:
            pyttsx3.speak("camera will open in a second")
            os.system("start microsoft.windows.camera:")
            continue
    elif ("camera" in p) and ("close"in p):
        pyttsx3.speak(" closing camera")
        os.system("taskkill/im windowscamera.exe")

    elif ("email"in p)and (("run" in p) or ("open" in p)):
        if "dont" in p:
            pyttsx3.speak("okk,as you say")
            pass
        else:
            pyttsx3.speak("e-mail will open in a second")
            os.system("start outlookmail:")
            continue
    elif ("email" in p) and ("close"in p):
        pyttsx3.speak(" closing mail")
        os.system("taskkill/im commsapps.exe")

    elif  (("map"in p)or("location"in p))and (("show"in p)or("run" in p) or ("open" in p)):
        if "dont" in p:
            pyttsx3.speak("okk,as you say")
            pass
        else:
            pyttsx3.speak("map will open in a second")
            os.system("start bingmaps:")
            continue
    elif (("map" in p) or ("location" in p)) and ("close"in p):
        pyttsx3.speak(" closing maps")
        os.system("taskkill/im maps.exe")

    elif ("news" in p)and (("run" in p) or ("open" in p)or ("show" in p)):
        if "dont" in p:
            pyttsx3.speak("okk,as you say")
            pass
        else:
            pyttsx3.speak("news will open in a second")
            os.system("start bingnews:")
            continue
    elif ("news" in p) and ("close"in p):
        pyttsx3.speak(" closing news")
        os.system("taskkill/im Microsoft.Msn.News.exe")

    elif ("screenshot" in p) and (("take"in p) or("run" in p) or ("open" in p)):
        if "dont" in p:
            pyttsx3.speak("okk,as you say")
            pass
        else:
            pyttsx3.speak("Snip & Sketch will open in a second")
            os.system("start ms-ScreenSketch:")
            continue
    elif ("screenshot" in p) and ("close"in p):
        pyttsx3.speak(" closing snip&sketch")
        os.system("taskkill/im ScreenSketch.exe")

    elif ("Excel" in p)and (("run" in p) or ("open" in p)):
        if "dont" in p:
            pyttsx3.speak("okk,as you say")
            pass
        else:
            pyttsx3.speak("microsoft excel will open in a second")
            os.system("start excel")
            continue
    elif ("Excel" in p) and ("close"in p):
        pyttsx3.speak(" closing msexcel")
        os.system("taskkill/im excel.exe")

    elif ("MS Word" in p or "Word" in p) and (("run" in p) or ("open" in p)):
        if "dont" in p:
            pyttsx3.speak("okk,as you say")
            pass
        else:
            pyttsx3.speak("microsoft word will open in a second")
            os.system("start winword")
            continue
    elif ("MS Word" in p or "Word" in p) and ("close"in p):
        pyttsx3.speak(" closing ms word")
        os.system("taskkill/im winword.exe")

    elif ("Adobe Reader"in p) and (("run" in p) or ("open" in p)):
        if "dont" in p:
            pyttsx3.speak("okk,as you say")
            pass
        else:
            pyttsx3.speak("adobe reader will open in a second")
            os.system("start acrord32")
            continue
    elif ("Adobe Reader" in p) and ("close"in p):
        pyttsx3.speak(" closing adobe reader")
        os.system("taskkill/im acrord32.exe")

    elif ("PowerPoint" in p)and (("run" in p) or ("open" in p)):
        if "dont" in p:
            pyttsx3.speak("okk,as you say")
            pass
        else:
            pyttsx3.speak("powerpoint will open in a second")
            os.system("start powerpnt")
            continue
    elif ("PowerPoint" in p) and ("close"in p):
        pyttsx3.speak(" closing powerpoint")
        os.system("taskkill/im  powerpnt.exe")

    elif("exit" in p) or ("quit"in p):
        pyttsx3.speak("exiting the program. have a good day")
        break
    elif "help" in p:
        print()
        print("\t\tTHINGS PAPPU CAN DO")
        print("\tI can open and close some applications\n ")
        print("chrome,notepad,media player,calculator,my pc,vlc media player,virtualbox,\nms paint,task manager,calendar,clock,camera,email,maps,news,screenshot,\nmicrosoft excel,microsoft powerpoint,microsoft word,adobe reader")
        print("\n\n")
    else:
        pyttsx3.speak("unable to recognize what you have said.")
        
