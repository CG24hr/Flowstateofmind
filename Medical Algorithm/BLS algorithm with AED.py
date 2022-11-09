print("Verify scene safety")
print("Check for responsiveness and shout for nearby help")
print("Call 1669")
print("send someone to get AED and emergency equipment")
Breathing = input("Is patient breathing?<Y/N>")
if Breathing == "Y" :
    print("Monitor until emergency responders arrive.")
if Breathing == "N" :
    print("Start CPR and use AED as soon as it is available")
    ShockableRhythm = input("AED shows Shockable Rhythm(Y/N>:")
    if ShockableRhythm == "Y" :
        print("Give 1 shock, Resume CPR immediately for 2 minutes")
    else :
        print("Resume CPR immediately for 2 minutes")
