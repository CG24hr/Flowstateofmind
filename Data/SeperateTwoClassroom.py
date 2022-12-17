# ID, Mr/Ms, Name, Score<0-100> : n = 300
# use DataFrame for data manipulating
# group sampling for equality of score 

n = int(input('Number of students : '))
ID = []
Gender = []
Score = []


import random 
for i in range(1,n+1) :
    ID.append(i) # create ID respectively
    sex = random.choice(['Male','Female'])
    Gender.append(sex) # random gender 
    points = random.randint(20,96) # random student score
    Score.append(points)
print(ID)
print(Gender)
print(Score)

import numpy as np 
ID_np = np.array(ID)
Gender_np = np.array(Gender)
Score_np = np.array(Score)

Class = {}
Class['ID'] = ID_np
Class['Gender'] = Gender_np
Class['Score'] = Score_np

import pandas as pd

allroom = pd.DataFrame(Class)
allroom = allroom.set_index('ID')
print(allroom)
print(allroom.describe())

Grade = []
for i in allroom['Score'] :
    if i >= 80 :
        Grade.append('A')
    elif 60 <= i < 80 :
        Grade.append('B')
    elif 50 <= i < 60 :
        Grade.append('C')
    else :
        Grade.append('D')

Grade_np = np.array(Grade)
allroom['Grade'] = Grade_np
allroom = allroom.sort_values(['Grade'])
print(allroom)

# separate into 2 classrooms
classOne = allroom.iloc[0::2]
classTwo = allroom.iloc[1::2]
print(classOne)
print(classTwo)
print(classOne.describe())
print(classTwo.describe())


