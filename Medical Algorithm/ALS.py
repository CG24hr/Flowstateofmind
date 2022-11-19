def unshockable(cycle) :
    print('Possible Asystole/PEA.')
    print('CPR for 2 minutes, Give IV epinephrine 1 mg every 3-5 minutes.')
    cycle = cycle + 1
    print('cycle' , cycle)
    rhythm = input('Is rhyhtm shockable?<Yes/No> :')
    if rhythm == 'Yes' :
        shockableWithEpinephrine(cycle)
        rhythm = input('Is rhyhtm shockable?<Yes/No> :')
        if rhythm == 'Yes' :
            shockableWithAmiodarone(shockableWithEpinephrine(cycle))
        if rhythm == 'No' :
            unshockable(cycle)
    if rhythm == 'No' :
        unshockable(cycle)


def shockable(cycle) :
    rhythm = input('Is rhyhtm shockable?<Yes/No> :')
    if rhythm == 'Yes' :
        shockableWithEpinephrine(cycle)
        rhythm = input('Is rhyhtm shockable?<Yes/No> :')
        if rhythm == 'Yes' :
            shockableWithAmiodarone(shockableWithEpinephrine(cycle))
        if rhythm == 'No' :
            unshockable(cycle)
    if rhythm == 'No' :
        unshockable(cycle)


def shockableWithEpinephrine(cycle) :
    print('Give 1 shock, continue CPR for 2 minutes and Give epinephrine 1 mg IV every 3-5 minutes.')
    cycle = cycle + 1
    print('cycle' , cycle)
    return cycle

def shockableWithAmiodarone(cycle) :
    print('Give 1 shock, continue CPR for 2 minutes and Give IV amiodarone 300 mg IV in first dose, then 150 mg IV in next dose.')
    cycle = cycle + 1
    print('cycle' , cycle)
    shockable(cycle)



print('Start CPR.')
print('Give Oxygen and attach monitor/defibrillator.')
rhythm = input('Is rhyhtm shockable?<Yes/No> :')
cycle = 0 
if rhythm == 'Yes' : 
    print('Possible VF/pulselessVT.')
    print('Give 1 shock, continue CPR for 2 minutes.')
    cycle = cycle + 1
    print('cycle' , cycle)
    shockable(cycle)
if rhythm == 'No' :
    unshockable(cycle)
        
        

