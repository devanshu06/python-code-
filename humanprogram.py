#Problem is :- "Convert the OS based program into a menu driven program using Python Code which will execute the required user query when user will give the input as a text."
import pyttsx3
import os
pyttsx3.speak("welcome to my personal assistant pappu")
print()
while True:
    x= print("PAPPU: what should i do for you?")
    p= input("USER:")
    if("chrome" in p) and (("run" in p) or ("open" in p)):
        if "dont"in p:
           pyttsx3.speak("okk,as you say")
           pass
        else:
           pyttsx3.speak("chrome will open in a second")
           os.system("start chrome")
           continue
    elif("chrome" in p)and("close"in p):
        pyttsx3.speak("closing chrome")
        os.system("taskkill/im chrome.exe")
    elif("notepad" in p) and (("run" in p) or ("open" in p)):
        if "dont"in p:
           pyttsx3.speak("okk,as you say")
           pass
        else:
           pyttsx3.speak("notepad will open in a second")
           os.system("start notepad")
           continue
    elif("notepad" in p) and ("close"in p):
        pyttsx3.speak("closing notepad")
        os.system("taskkill/im notepad.exe")
    elif("window media" in p) and (("run" in p) or ("open" in p)):
        if "dont"in p:
           pyttsx3.speak("okk,as you say")
           pass
        else:
           pyttsx3.speak("window media player will open in a second")
           os.system("start wmplayer")
           continue
    elif ("window media" in p) and ("close"in p):
        pyttsx3.speak("closing window media player")
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
    elif("mycomputer" in p) and (("open" in p) or ("run" in p)):
        if "dont"in p:
           pyttsx3.speak("okk,as you say")
           pass
        else:
           pyttsx3.speak("my computer will open in a second")
           os.system("start explorer")
           continue
    elif ("mycomputer" in p) and ("close"in p):
        pyttsx3.speak("access denied to close")
    elif("vlc" in p) and (("run" in p) or ("open" in p)):
        if "dont"in p:
           pyttsx3.speak("okk,as you say")
           pass
        else:
           pyttsx3.speak("vlc media player will open in a second")
           os.system("start vlc")
           continue
    elif ("vlc" in p) and ("close"in p):
        pyttsx3.speak("closing vlc media player")
        os.system("taskkill/im vlc.exe")
    elif("virtualmachine"in p ) and (("run" in p) or ("open" in p)):
        if "dont"in p:
           pyttsx3.speak("okk,as you say")
           pass
        else:
           pyttsx3.speak("virtual machine will open in a second")
           os.system("start virtualbox")
           continue
    elif ("virtualmachine" in p) and ("close"in p):
        pyttsx3.speak("closing virtual machine")
        os.system("taskkill/im virtualbox.exe")
    elif("mspaint" in p) and (("run" in p) or ("open" in p)):
        if "dont"in p:
           pyttsx3.speak("okk,as you say")
           pass
        else:
           pyttsx3.speak("paint will open in a second")
           os.system("start mspaint")
           continue
    elif ("mspaint" in p) and ("close"in p):
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
    elif ("news" in p)and (("run" in p) or ("open" in p)):
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
    elif ("excel" in p)and (("run" in p) or ("open" in p)):
        if "dont" in p:
            pyttsx3.speak("okk,as you say")
            pass
        else:
            pyttsx3.speak("microsoft excel will open in a second")
            os.system("start excel")
            continue
    elif ("excel" in p) and ("close"in p):
        pyttsx3.speak(" closing msexcel")
        os.system("taskkill/im excel.exe")
    elif ("msword" in p)and (("run" in p) or ("open" in p)):
        if "dont" in p:
            pyttsx3.speak("okk,as you say")
            pass
        else:
            pyttsx3.speak("microsoft word will open in a second")
            os.system("start winword")
            continue
    elif ("msword" in p) and ("close"in p):
        pyttsx3.speak(" closing ms word")
        os.system("taskkill/im winword.exe")
    elif ("adobe reader"in p) and (("run" in p) or ("open" in p)):
        if "dont" in p:
            pyttsx3.speak("okk,as you say")
            pass
        else:
            pyttsx3.speak("adobe reader will open in a second")
            os.system("start acrord32")
            continue
    elif ("adobe reader" in p) and ("close"in p):
        pyttsx3.speak(" closing adobe reader")
        os.system("taskkill/im acrord32.exe")
    elif ("powerpoint" in p)and (("run" in p) or ("open" in p)):
        if "dont" in p:
            pyttsx3.speak("okk,as you say")
            pass
        else:
            pyttsx3.speak("powerpoint will open in a second")
            os.system("start powerpnt")
            continue
    elif ("powerpoint" in p) and ("close"in p):
        pyttsx3.speak(" closing powerpoint")
        os.system("taskkill/im  powerpnt.exe")
    elif("exit" in p) or ("quit"in p):
        pyttsx3.speak("exiting the program. have a good day")
        print("Have a good day...")
        break
    elif "help" in p:
        print()
        print("\t\tTHINGS PAPPU CAN DO")
        print("\tI can open and close some applications\n ")
        print("chrome,notepad,media player,calculator,my pc,vlc media player,virtualbox,\nms paint,task manager,calendar,clock,camera,email,maps,news,screenshot,\nmicrosoft excel,microsoft powerpoint,microsoft word,adobe reader")
        print("\n\n")
    else:
        pyttsx3.speak("unable to understand what you have written.")
        print("Not able to understand")

