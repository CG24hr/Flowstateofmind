print("Verify scene safety")
print("Check for responsiveness and shout for nearby help")
print("Call 1669")
print("send someone to get AED and emergency equipment")

Breathing = input("Is patient breathing?<Yes/No/Abnormal> :")
Pulse = input("Do you feel patient's pulse within 5-10 seconds?<Yes/No> :")
if Pulse == "Yes" :
    if Breathing == "Yes" :
        print("Monitor until emergency responder arrive.")
    elif Breathing == "Abnormal" :
        print("Check pulse every 2 minutes.; If no pulse, start CPR.")
        print("if possible opiod overdose, administer naloxone if available.")
    else :
        print("Please check breathing again.")
if Pulse == "No" :
    print("Start CPR until AED arrives.")
    print("Continually perform cycles of 30 compressions and 2 breaths.")
    print("If AED arrives, Check the rhythm.")
    cycle = 0
    while cycle >= 0 :
        shockableRhythm = input("Shockable?<Yes/No> :")
        if shockableRhythm == "Yes" :
            print("Give 1 shock and resume CPR immediately for 2 minutes.")
            cycle = cycle + 1
        if shockableRhythm == "No" :
            Pulse = input("Do you feel patient's pulse within 5-10 seconds?<Yes/No> :")
            if Pulse == "No" :
                print("Resume CPR immediately for 2 minutes.")
                cycle = cycle + 1
            if Pulse == "Yes" :
                print("Monitor until emergency responder arrive.")
                break
        print("Cycle",cycle)
        print("Continue until Advanced Life Support Providers take over.")
    
       

