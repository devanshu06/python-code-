#Problem is :- "Convert the OS based program into a menu driven program using Python Code which will execute the required user query when user will give the input as a text."
import pyttsx3
import os
pyttsx3.speak("welcome to my tool, here are some thing that my tool can do")
pyttsx3.speak("it can run some programs like")
pyttsx3.speak("chrome , notepad , mediaplayer , calculator , my pc , vlc media player , virtualbox , ms paint , task manager , calendar , clock , camera , email , maps , news , screenshot , microsoft excel , microsoft powerpoint , microsoft word , adobe reader")
print()
while True:
    p = input("enter what you want to open :")
    if(("chrome" in p) or ("google" in p) or ("browser" in p)) and (("run" in p) or ("open" in p) or ("excute" in p)):
        if ("dont"in p)or("dont"in p)or("do not" in p):
           pass
        else:
           pyttsx3.speak("chrome will open in a second")
           os.system("start chrome")
           continue
    elif(("chrome" in p) or ("google" in p) or ("browser" in p))and("close"in p):
        pyttsx3.speak("closing chrome")
        os.system("taskkill/im chrome.exe")

    elif(("text") in p or ("editor") in p or ("notepad") in p) and (("run" in p) or ("open" in p) or ("excute" in p)):
        if ("dont"in p)or("dont"in p)or("do not" in p):
           pass
        else:
           pyttsx3.speak("notepad will open in a second")
           os.system("start notepad")
           continue
    elif(("text") in p or ("editor") in p or ("notepad") in p) and ("close"in p):
        pyttsx3.speak("closing notepad")
        os.system("taskkill/im notepad.exe")

    elif(("music" in p) or ("media" in p) or ("songs" in p) or ("song" in p)) and (("play" in p) or ("run" in p) or ("open" in p) or ("excute" in p)):
        if ("dont"in p)or("dont"in p)or("do not" in p):
           pass
        else:
           pyttsx3.speak("window media player will open in a second")
           os.system("start wmplayer")
           continue
    elif (("music" in p) or ("media" in p) or ("songs" in p) or ("song" in p)) and ("close"in p):
        pyttsx3.speak("closing window media player")
        os.system("taskkill/im wmplayer.exe")

    elif(("calc" in p) or ("calculator" in p)) and (("open" in p) or ("run" in p)):
        if ("dont"in p)or("dont"in p)or("do not" in p):
           pass
        else:
           pyttsx3.speak("calculator will open in a second")
           os.system("start calc")
           continue
    elif (("calc" in p) or ("calculator" in p)) and ("close"in p):
        pyttsx3.speak("closing calculator")
        os.system("taskkill/im calculator.exe")

    elif(("mycomputer" in p) or ("pc" in p)) and (("open" in p) or ("run" in p) or ("excute" in p)):
        if ("dont"in p)or("dont"in p)or("do not" in p):
           pass
        else:
           pyttsx3.speak("my computer will open in a second")
           os.system("start explorer")
           continue
    elif (("mycomputer" in p) or ("pc" in p)) and ("close"in p):
        pyttsx3.speak("access denied to close")


    elif(("video" in p) or ("videos" in p) or ("vlc" in p)) and (("play" in p) or ("run" in p) or ("open" in p) or ("excute" in p)):
        if ("dont"in p)or("dont"in p)or("do not" in p):
           pass
        else:
           pyttsx3.speak("vlc media player will open in a second")
           os.system("start vlc")
           continue
    elif (("video" in p) or ("videos" in p) or ("vlc" in p)) and ("close"in p):
        pyttsx3.speak("closing vlc media player")
        os.system("taskkill/im vlc.exe")

    elif(("virtual") in p or ("terminal") in p or("machine")in p ) and (("run" in p) or ("open" in p) or ("excute" in p)):
        if ("dont"in p)or("dont"in p)or("do not" in p):
           pass
        else:
           pyttsx3.speak("virtual machine will open in a second")
           os.system("start virtualbox")
           continue
    elif (("virtual") in p or ("terminal") in p or ("machine") in p) and ("close"in p):
        pyttsx3.speak("closing virtual machine")
        os.system("taskkill/im virtualbox.exe")


    elif(("paint") in p or ("ms") in p or ("3d" in p ) ) and (("run" in p) or ("open" in p) or ("excute" in p)):
        if ("dont"in p)or("dont"in p)or("do not" in p):
           pass
        else:
           pyttsx3.speak("paint will open in a second")
           os.system("start mspaint")
           continue
    elif (("paint") in p or ("ms") in p or ("3d" in p)) and ("close"in p):
        pyttsx3.speak("closing paint")
        os.system("taskkill/im mspaint.exe")

    elif(("task"in p) or ("manager" in p)) and (("run" in p) or ("open" in p) or ("excute" in p)):
        if ("dont"in p)or("dont"in p)or("do not" in p):
           pass
        else:
           pyttsx3.speak("task manager will open in a second")
           os.system("start taskmgr")
           continue
    elif (("task" in p) or ("manager" in p)) and ("close"in p):
        pyttsx3.speak(" access denied to close")

    elif("calendar" in p) and (("run" in p) or ("open" in p) or ("excute" in p)):
        if ("dont"in p)or("dont"in p)or("do not" in p):
           pass
        else:
           pyttsx3.speak("calendar will open in a second")
           os.system("start outlookcal:")
           continue
    elif ("calendar" in p) and ("close"in p):
        pyttsx3.speak(" access denied to close")

    elif (("clock" in p) or ("time"in p))and (("show" in p) or ("run" in p) or ("open" in p) or ("excute" in p)):
        if ("dont" in p) or ("dont" in p) or ("do not" in p):
            pass
        else:
            pyttsx3.speak("clock will open in a second")
            os.system("start ms-clock:")
            continue
    elif (("clock" in p) or ("time" in p)) and ("close"in p):
        pyttsx3.speak(" closing clock")
        os.system("taskkill/im time.exe")

    elif (("camera" in p) or ("webcam"in p))and (("run" in p) or ("open" in p) or ("excute" in p)):
        if ("dont" in p) or ("dont" in p) or ("do not" in p):
            pass
        else:
            pyttsx3.speak("camera will open in a second")
            os.system("start microsoft.windows.camera:")
            continue
    elif (("camera" in p) or ("webcam" in p)) and ("close"in p):
        pyttsx3.speak(" closing camera")
        os.system("taskkill/im windowscamera.exe")

    elif (("mail" in p) or ("email"in p))and (("run" in p) or ("open" in p) or ("excute" in p)):
        if ("dont" in p) or ("dont" in p) or ("do not" in p):
            pass
        else:
            pyttsx3.speak("e-mail will open in a second")
            os.system("start outlookmail:")
            continue
    elif (("mail" in p) or ("email" in p)) and ("close"in p):
        pyttsx3.speak(" closing mail")
        os.system("taskkill/im commsapps.exe")

    elif (("maps" in p) or ("map"in p)or("location"in p))and (("show"in p)or("run" in p) or ("open" in p) or ("excute" in p)):
        if ("dont" in p) or ("dont" in p) or ("do not" in p):
            pass
        else:
            pyttsx3.speak("map will open in a second")
            os.system("start bingmaps:")
            continue
    elif (("maps" in p) or ("map" in p) or ("location" in p)) and ("close"in p):
        pyttsx3.speak(" closing maps")
        os.system("taskkill/im maps.exe")

    elif (("news" in p))and (("show"in p)or("run" in p) or ("open" in p) or ("excute" in p)):
        if ("dont" in p) or ("dont" in p) or ("do not" in p):
            pass
        else:
            pyttsx3.speak("news will open in a second")
            os.system("start bingnews:")
            continue
    elif (("news" in p)) and ("close"in p):
        pyttsx3.speak(" closing news")
        os.system("taskkill/im Microsoft.Msn.News.exe")

    elif (("screenshot" in p) or ("snap" in p) or("snip"in p)or("sketch"in p)) and (("take"in p) or("run" in p) or ("open" in p) or ("excute" in p)):
        if ("dont" in p) or ("dont" in p) or ("do not" in p):
            pass
        else:
            pyttsx3.speak("Snip & Sketch will open in a second")
            os.system("start ms-ScreenSketch:")
            continue
    elif (("screenshot" in p) or ("snap" in p) or ("snip" in p)or("sketch"in p)) and ("close"in p):
        pyttsx3.speak(" closing snip&sketch")
        os.system("taskkill/im ScreenSketch.exe")

    elif (("excel" in p)or ("sheet"in p))and (("run" in p) or ("open" in p) or ("excute" in p)):
        if ("dont" in p) or ("dont" in p) or ("do not" in p):
            pass
        else:
            pyttsx3.speak("microsoft excel will open in a second")
            os.system("start excel")
            continue
    elif (("excel" in p) or ("sheet" in p)) and ("close"in p):
        pyttsx3.speak(" closing msexcel")
        os.system("taskkill/im excel.exe")

    elif (("word" in p)or ("office"in p))and (("run" in p) or ("open" in p) or ("excute" in p)):
        if ("dont" in p) or ("dont" in p) or ("do not" in p):
            pass
        else:
            pyttsx3.speak("microsoft word will open in a second")
            os.system("start winword")
            continue
    elif (("word" in p) or ("office" in p)) and ("close"in p):
        pyttsx3.speak(" closing msword")
        os.system("taskkill/im winword.exe")

    elif (("adobe" in p)or ("reader"in p)or ("pdf"in p)or("viewer"in p))and (("run" in p) or ("open" in p) or ("excute" in p)):
        if ("dont" in p) or ("dont" in p) or ("do not" in p):
            pass
        else:
            pyttsx3.speak("adobe reader will open in a second")
            os.system("start acrord32")
            continue
    elif (("adobe" in p) or ("reader" in p) or ("pdf" in p) or ("viewer" in p)) and ("close"in p):
        pyttsx3.speak(" closing adobe reader")
        os.system("taskkill/im acrord32.exe")

    elif (("powerpoint" in p)or ("presentation"in p))and (("run" in p) or ("open" in p) or ("excute" in p)):
        if ("dont" in p) or ("dont" in p) or ("do not" in p):
            pass
        else:
            pyttsx3.speak("powerpoint will open in a second")
            os.system("start powerpnt")
            continue
    elif (("powerpoint" in p) or ("presentation" in p)) and ("close"in p):
        pyttsx3.speak(" closing powerpoint")
        os.system("taskkill/im  powerpnt.exe")

    elif (("exit" in p) or ("terminate" in p) or ("quit"in p)):
        pyttsx3.speak("exiting the program. have a good day")
        print("Have a good day...")
        break
    else:
        pyttsx3.speak("unable to understand what you have written.")
        print("Not able to understand")



