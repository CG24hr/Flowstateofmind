# Create Manchester United seasonal dataframe : row = seasons, column = possession + goal + manager

import pandas as pd 
N = int(input('Number of seasons : '))
count = 0 
seasons = []
possession = []
goal = []
manager = []
while count < N :
    year = input('Season' + str(count+1) + ':')
    seasons.append(year)
    P = int(input('Average possession per game : '))
    possession.append(P)
    G = float(input('Average goal per game : '))
    goal.append(G)
    M = input('Team manager : ')
    manager.append(M)
    manchesterunited = {}
    manchesterunited['AVG possession'] = possession
    manchesterunited['AVG goal'] = goal
    manchesterunited['Manager'] = manager
    count = count + 1
print(seasons)
print(manchesterunited)
statistics = pd.DataFrame(manchesterunited)
statistics.index = seasons # กำหนด index ของ rows
print(statistics)

# use .loc method for specific row & column display : str
print(statistics.loc[:, ['AVG possession', 'AVG goal']])
# use .iloc method for specific row & column display : index
print(statistics.iloc[:, [2]])

