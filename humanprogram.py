# import pyttsx3
# pyttsx3.speak("welcome to my tools")
import os
print()
while True:
    p = input("enter what you want to open :")
    if (("chrome" in p) or ("google" in p) or ("browser" in p)) and (("run" in p) or ("open" in p) or ("excute" in p)):
        if ("dont"in p):
           pass
        else:
           os.system("chrome")
           continue
    elif (("text") in p or ("editor") in p or ("notepad") in p) and (("run" in p) or ("open" in p) or ("excute" in p)):
        if ("dont"in p):
           pass
        else:
           os.system("start notepad")
           continue
    elif (("music" in p) or ("media" in p) or ("songs" in p) or ("song" in p)) and (("play" in p) or ("run" in p) or ("open" in p) or ("excute" in p)):
        if ("dont"in p):
           pass
        else:
           os.system("start wmplayer")
           continue
    elif (("calc" in p) or ("calculator" in p)or("cal" in p)) and (("open" in p) or ("run" in p)):
        if ("dont"in p):
           pass
        else:
           os.system("calc")
           continue
    elif (("computer" in p) or ("pc" in p)) and (("open" in p) or ("run" in p) or ("excute" in p)):
        if ("dont"in p):
           pass
        else:
           os.system("explorer")
           continue
    elif (("video" in p) or ("media" in p) or ("videos" in p) or ("vlc" in p)) and (("play" in p) or ("run" in p) or ("open" in p) or ("excute" in p)):
        if ("dont"in p):
           pass
        else:
           os.system("start vlc")
           continue
    elif (("exit" in p) or ("terminate" in p) or ("end"in p)):
        break
    else:
        print("Don't Support")

