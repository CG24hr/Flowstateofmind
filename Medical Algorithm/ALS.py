print('Start CPR.')
print('Give Oxygen and attach monitor/defibrillator.')
shock = input('Is rhyhtm shockable?<Yes/No> :')
cycle = 0 

def shockable() :
    if shock == 'Yes' :
        print('Possible VF/pVT')
        print('Give 1 shock and continue CPR for 2 minutes')
        cycle = cycle + 1
        print('cycle' , cycle)
        shock = input('Is rhyhtm shockable?<Yes/No> :')
        while shock == "Yes" :
            print('CPR 2 minutes , Give epinephrine 1 mg IV every 3-5 minutes.')
            cycle = cycle + 1
            print('cycle' , cycle)
            shock = input('Is rhyhtm shockable?<Yes/No> :')
            if shock == "Yes" :
                print('CPR 2 minutes , Give Amiodarone 300 mg IV in first single dose ,then 150 mg in next dose.)')
                print('Treat reversible causes')
                cycle = cycle + 1 
                print('cycle' , cycle)
                shock = input('Is rhyhtm shockable?<Yes/No> :')
            if shock == "No" :
                return unshockable()
def unshockable() :
    if shock == 'No' :
        while shock == 'No' :
            print('Possible Asystole/PEA')
            print('CPR 2 minutes , Give epinephrine 1 mg IV every 3-5 minutes.')
            cycle = cycle + 1
            print('cycle' , cycle)
            shock = input('Is rhyhtm shockable?<Yes/No> :')
        
        

