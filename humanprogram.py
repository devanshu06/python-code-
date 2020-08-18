#Problem is :- "Convert the OS based program into a menu driven program using Python Code which will execute the required user query when user will give the input as a text."
import pyttsx3
import os
pyttsx3.speak("welcome to my tool, here are some thing that my tool can do")
pyttsx3.speak("it can run some programs like")
pyttsx3.speak("chrome , notepad , mediaplayer , calculator , my pc , vlc media player , virtualbox , ms paint , task manager , calendar , clock , camera , email , maps , news , photos , setting , screenshot , weather , window defender , xbox")
print()
while True:
    p = input("enter what you want to open :")
    if(("chrome" in p) or ("google" in p) or ("browser" in p)) and (("run" in p) or ("open" in p) or ("excute" in p)):
        if ("dont"in p)or("dont"in p)or("do not" in p):
           pass
        else:
           pyttsx3.speak("chrome will open in a second")
           os.system("chrome")
           continue
    elif(("text") in p or ("editor") in p or ("notepad") in p) and (("run" in p) or ("open" in p) or ("excute" in p)):
        if ("dont"in p)or("dont"in p)or("do not" in p):
           pass
        else:
           pyttsx3.speak("notepad will open in a second")
           os.system("start notepad")
           continue
    elif(("music" in p) or ("media" in p) or ("songs" in p) or ("song" in p)) and (("play" in p) or ("run" in p) or ("open" in p) or ("excute" in p)):
        if ("dont"in p)or("dont"in p)or("do not" in p):
           pass
        else:
           pyttsx3.speak("window media player will open in a second")
           os.system("start wmplayer")
           continue
    elif(("calc" in p) or ("calculator" in p)) and (("open" in p) or ("run" in p)):
        if ("dont"in p)or("dont"in p)or("do not" in p):
           pass
        else:
           pyttsx3.speak("calculator will open in a second")
           os.system("calc")
           continue
    elif(("computer" in p) or ("pc" in p)) and (("open" in p) or ("run" in p) or ("excute" in p)):
        if ("dont"in p)or("dont"in p)or("do not" in p):
           pass
        else:
           pyttsx3.speak("my computer will open in a second")
           os.system("explorer")
           continue
    elif(("video" in p) or ("media" in p) or ("videos" in p) or ("vlc" in p)) and (("play" in p) or ("run" in p) or ("open" in p) or ("excute" in p)):
        if ("dont"in p)or("dont"in p)or("do not" in p):
           pass
        else:
           pyttsx3.speak("vlc media player will open in a second")
           os.system("start vlc")
           continue

    elif(("virtual") in p or ("terminal") in p or("machine")in p ) and (("run" in p) or ("open" in p) or ("excute" in p)):
        if ("dont"in p)or("dont"in p)or("do not" in p):
           pass
        else:
           pyttsx3.speak("virtual machine will open in a second")
           os.system("start virtualbox")
           continue
    elif(("paint") in p or ("ms") in p or ("3d" in p ) ) and (("run" in p) or ("open" in p) or ("excute" in p)):
        if ("dont"in p)or("dont"in p)or("do not" in p):
           pass
        else:
           pyttsx3.speak("paint will open in a second")
           os.system("start mspaint")
           continue
    elif(("task") in p or ("manager") in p or ("kill" in p ) ) and (("run" in p) or ("open" in p) or ("excute" in p)):
        if ("dont"in p)or("dont"in p)or("do not" in p):
           pass
        else:
           pyttsx3.speak("task manager will open in a second")
           os.system("start taskmgr")
           continue
    elif("calendar" in p) and (("run" in p) or ("open" in p) or ("excute" in p)):
        if ("dont"in p)or("dont"in p)or("do not" in p):
           pass
        else:
           pyttsx3.speak("calendar will open in a second")
           os.system("start outlookcal:")
           continue
    elif (("clock" in p) or ("time"in p))and (("show" in p) or ("run" in p) or ("open" in p) or ("excute" in p)):
        if ("dont" in p) or ("dont" in p) or ("do not" in p):
            pass
        else:
            pyttsx3.speak("clock will open in a second")
            os.system("start ms-clock:")
            continue
    elif (("camera" in p) or ("webcam"in p))and (("run" in p) or ("open" in p) or ("excute" in p)):
        if ("dont" in p) or ("dont" in p) or ("do not" in p):
            pass
        else:
            pyttsx3.speak("camera will open in a second")
            os.system("start microsoft.windows.camera:")
            continue
    elif (("mail" in p) or ("email"in p))and (("run" in p) or ("open" in p) or ("excute" in p)):
        if ("dont" in p) or ("dont" in p) or ("do not" in p):
            pass
        else:
            pyttsx3.speak("e-mail will open in a second")
            os.system("start outlookmail:")
            continue
    elif (("maps" in p) or ("map"in p)or("location"in p))and (("show"in p)or("run" in p) or ("open" in p) or ("excute" in p)):
        if ("dont" in p) or ("dont" in p) or ("do not" in p):
            pass
        else:
            pyttsx3.speak("map will open in a second")
            os.system("start bingmaps:")
            continue
    elif (("news" in p))and (("show"in p)or("run" in p) or ("open" in p) or ("excute" in p)):
        if ("dont" in p) or ("dont" in p) or ("do not" in p):
            pass
        else:
            pyttsx3.speak("news will open in a second")
            os.system("start bingnews:")
            continue
    elif (("photos" in p)or("photo"in p)or("picture"in p)or("pic"in p))and (("show"in p)or("run" in p) or ("open" in p) or ("excute" in p)):
        if ("dont" in p) or ("dont" in p) or ("do not" in p):
            pass
        else:
            pyttsx3.speak("photos will open in a second")
            os.system("start ms-photos:")
            continue
    elif (("setting" in p)or("settings" in p))and (("show"in p)or("run" in p) or ("open" in p) or ("excute" in p)):
        if ("dont" in p) or ("dont" in p) or ("do not" in p):
            pass
        else:
            pyttsx3.speak("setting will open in a second")
            os.system("start ms-settings:")
            continue
    elif (("screenshot" in p) or ("snap" in p) or("snip"in p)) and (("take"in p) or("run" in p) or ("open" in p) or ("excute" in p)):
        if ("dont" in p) or ("dont" in p) or ("do not" in p):
            pass
        else:
            pyttsx3.speak("Snip & Sketch will open in a second")
            os.system("start ms-ScreenSketch:")
            continue
    elif (("weather" in p)or("forecast" in p)or("temprature"in p))and (("today","yesterday","tommorow"in p) or("run" in p) or ("open" in p) or ("excute" in p)):
        if ("dont" in p) or ("dont" in p) or ("do not" in p):
            pass
        else:
            pyttsx3.speak("weather will open in a second")
            os.system("start bingweather:")
            continue
    elif (("scanner" in p)or("defender" in p)or("antivirus"in p))and (("run" in p) or ("open" in p) or ("excute" in p)):
        if ("dont" in p) or ("dont" in p) or ("do not" in p):
            pass
        else:
            pyttsx3.speak("window defender will open in a second")
            os.system("start windowsdefender:")
            continue
    elif (("xbox" in p)or("gaming" in p)or("console"in p)or("game"in p))and (("run" in p) or ("open" in p) or ("excute" in p)):
        if ("dont" in p) or ("dont" in p) or ("do not" in p):
            pass
        else:
            pyttsx3.speak("xbox will open in a second")
            os.system("start xbox:")
            continue
    elif (("exit" in p) or ("terminate" in p) or ("end"in p)):
        pyttsx3.speak("exiting the program.")
        break
    else:
        pyttsx3.speak("unable to understand what you have written.")
        print("not able to understand")

