# create bar chart to compare average possession between asian team
# create line plot for cumulative sum of goals and assists
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

WC = pd.read_csv('D:\\Users\\Desktop\\Python code\\GitHub\\Flowstateofmind\\Data\\csv\\Fifa_world_cup_matches.csv')
print(WC)
print(WC.index)

#asian : index = game possession, column = team
asian = ['QATAR', 'KOREA REPUBLIC', 'JAPAN', 'SAUDI ARABIA', 'IRAN', 'AUSTRALIA']
nation_home = []
possession_home = []
nation_away = []
possession_away = []
for index, rows in WC.iterrows() : 
    if rows['team1'] in asian :
        nation_home.append(rows['team1'])
        possession_home.append(rows['possession team1'])
    elif rows['team2'] in asian :
        nation_away.append(rows['team2'])
        possession_away.append(rows['possession team2'])
    else :
        None
nation_home = np.array(nation_home)
possession_home = np.array(possession_home)
nation_away = np.array(nation_away)
possession_away = np.array(possession_away)
print(nation_home)
print(possession_home)
print(nation_away)
print(possession_away)

asian_poss_1 = {}
asian_poss_1['nation'] = nation_home
asian_poss_1['possession'] = possession_home

asian_poss_2 = {}
asian_poss_2['nation'] = nation_away
asian_poss_2['possession'] = possession_away

print(asian_poss_1)
print(asian_poss_2)

asian_poss_home = pd.DataFrame(asian_poss_1)
asian_poss_away = pd.DataFrame(asian_poss_2)
asian_poss_home = asian_poss_home.sort_values('nation')
asian_poss_away = asian_poss_away.sort_values('nation')

def turnInt (str) : 
    str = str.replace('%', '')
    Integer = int(str)
    return Integer

asian_poss_home['possession'] = asian_poss_home['possession'].apply(turnInt)
asian_poss_away['possession'] = asian_poss_away['possession'].apply(turnInt)
print(asian_poss_home)
print(asian_poss_away)

# merge these two dataframes together vertically
asian_WC = pd.concat([asian_poss_home, asian_poss_away], sort = True).sort_values('nation')
print(asian_WC)
avg_asian_WC = asian_WC.groupby('nation')['possession'].agg(np.mean)
print(avg_asian_WC)

avg_asian_WC.plot(kind = 'bar')
plt.title('Average possession of Asian national teams in FIFA World cup 2022')
plt.xlabel('National teams')
plt.ylabel('Average possession')
plt.show()

# Line plot : total goals comparison between Argentina and France 
final_round = ['ARGENTINA', 'FRANCE']
final = WC[(WC['team1'].isin(final_round)) | (WC['team2'].isin(final_round))]
print(final)
final = final.loc[:, ['team1', 'team2', 'date', 'goal inside the penalty area team1', 'goal inside the penalty area team2', 'goal outside the penalty area team1', 'goal outside the penalty area team2']]
print(final)
final['goal team1'] = final['goal inside the penalty area team1'] + final['goal outside the penalty area team1']
final['goal team2'] = final['goal inside the penalty area team2'] + final['goal outside the penalty area team2']
final = final[['team1', 'team2', 'date', 'goal team1', 'goal team2']]
print(final)

final_1 = final.loc[:, ['team1', 'date','goal team1']]
final_1 = final_1[final_1['team1'].isin(final_round)]
final_2 = final.loc[:, ['team2', 'date', 'goal team2']]
final_2 = final_2[final_2['team2'].isin(final_round)]
print(final_1)
print(final_2)
final_1 = final_1.rename(columns = {'team1': 'team', 'goal team1' : 'goals'})
final_2 = final_2.rename(columns = {'team2': 'team', 'goal team2' : 'goals'})

FINAL = pd.concat([final_1, final_2], ignore_index = False)
FINAL = FINAL.sort_values('team')
print(FINAL)

total_goals_argentina = FINAL[FINAL['team'] == 'ARGENTINA']
total_goals_argentina['cumulative goals'] = total_goals_argentina['goals'].cumsum()
total_goals_france = FINAL[FINAL['team'] == 'FRANCE']
total_goals_france['cumulative goals'] = total_goals_france['goals'].cumsum()

total_goals_argentina = total_goals_argentina.reset_index()
total_goals_france = total_goals_france.reset_index()

print(total_goals_argentina)
print(total_goals_france)

total_goals = pd.concat([total_goals_argentina, total_goals_france])
total_goals = total_goals.loc[:, ['team', 'date', 'cumulative goals']]
print(total_goals)

total_goals_argentina = total_goals[total_goals['team'] == 'ARGENTINA']
total_goals_france = total_goals[total_goals['team'] == 'FRANCE']

plt.plot(total_goals_argentina.index, total_goals_argentina['cumulative goals'], marker = 'o')
plt.plot(total_goals_france.index, total_goals_france['cumulative goals'], marker = 'o')
plt.title('Cumulative goals comparison between Argentina and France national teams')
plt.xlabel('matches')
plt.ylabel('goals')
plt.show()

