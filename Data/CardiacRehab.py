# data = Age, LVEF, NYHA, SPPB
# number of participants = 10
    # use conditioning for include & exclude participants
    # inclusion criteria : age > 60, NYHA < 4 
    # exclusion criteria : severe dementia, Hx of ACS or HF within 1 month
    # use loop for inputting data
# import numpy to create array
# Import Pandas ->  row = participants , column : data 

n = int(input('Number of participants who were diagnosed with ADHF : '))
count = 0 
AGE = []
LVEF = []
NYHA = []
SPPB = []
while count < n :
    age = int(input(str(count+1) + ' Age : '))
    lvef = int(input(str(count+1) + ' LVEF(%) : '))
    nyha = int(input(str(count+1) + ' Functional class<1-4> : '))
    sppb = int(input(str(count+1) + ' SPPB<0-12> : '))
    dementia = input(str(count+1) + ' History of severe dementia<Y/N> : ')
    heart = input(str(count+1) + ' History of heart failure or myocardial infarction within 1 month <Y/N> : ')
    if age >= 60 and nyha < 4 and dementia == 'N' and heart == 'N' : # inclusion & exclusion criteria
        AGE.append(age)
        LVEF.append(lvef)
        NYHA.append(nyha)
        SPPB.append(sppb)
        print('This participant meet inclusion criteria.')
        count = count + 1    
    else : 
        print('This participant does not meet inclusion criteria.')
        count = count + 1
print('Total participants who met inclusion criteria is', len(AGE))


# ใช้ numpy create array เพื่อนำข้อมูลไปใส่ใน dictionary
import numpy as np 
AGE_np = np.array(AGE)
LVEF_np = np.array(LVEF)
NYHA_np = np.array(NYHA)
SPPB_np = np.array(SPPB)

N = len(AGE_np)
print('Total number of participants is', N)

dict = {}
dict['Age'] = AGE_np
dict['LVEF'] = LVEF_np
dict['NYHA'] = NYHA_np
dict['SPPB'] = SPPB_np

print(dict)


# นำข้อมูลใน dictionary มาสร้าง pandas dataframe
import pandas as pd 
patients = pd.DataFrame(dict)

participants = []
for i in range(1,N+1) :
    participants.append(i)

patients.index = participants
print(patients)
print(patients.describe())








