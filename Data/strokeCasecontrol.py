 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv('D:\\Users\\Desktop\\Python code\\GitHub\\Flowstateofmind\\Data\\csv\\healthcare-dataset-stroke-data.csv')
print(df)
df = df[['id', 'gender','age', 'hypertension', 'heart_disease', 'avg_glucose_level', 'bmi', 'smoking_status', 'stroke']]
df = df.set_index('id')
print(df)

# case control study : expected result -> Odd ratio between smoking and stroke relationships
# exclude other possible factors for stroke : HT, blood glucose > 125, bmi > 30
df_exclude = df[(df['hypertension'] == 0) & (df['avg_glucose_level'] < 125) & (df['bmi'] < 30)]
print(df_exclude)

# create dataframe of smoking & stroke relationships : calculate relative risk, 95% CI, p-value by chi-square
smoke = []
for index, rows in df_exclude.iterrows() : 
    if rows['smoking_status'] == 'formerly smoked' or rows['smoking_status'] == 'smokes' : 
        smoke.append('1')
    else : 
        smoke.append('0')
smoke = np.array(smoke)
df_exclude['Hx of smoking'] = smoke
df_smoke = df_exclude[['gender', 'age', 'Hx of smoking', 'stroke']]
print(df_smoke)

relations = df_smoke.groupby('Hx of smoking')['stroke'].value_counts()
# values = ค่าในตาราง, aggfunc ถ้าไม่ใส่ default คือการหาค่า mean
pivot_table = df_smoke.pivot_table(values = 'age', index = 'gender', aggfunc= [np.mean, np.median])
pivot_table2 = df.pivot_table(values = 'bmi', index = 'age', columns = 'smoking_status', aggfunc = np.mean, margins = True, fill_value = 0)
print(relations)
print(pivot_table)
print(pivot_table2)

ct = pd.crosstab(df_smoke['Hx of smoking'], df['stroke'])
print(ct)

import scipy.stats as stats
import math
def OR (a, b, c, d) : 
    OR = (a / b) * (d / c)
    CIlow, CIhigh = stats.norm.interval(0.95, OR, math.sqrt((1/a) + (1/b) + (1/c) + (1/d)))
    return OR, CIlow, CIhigh
 
def chi2 (a, b, c, d) : 
    table = np.array([[a,b], [c,d]]) # must be single array***
    chi2, pvalue, dof, expected = stats.chi2_contingency(table)
    return pvalue

Odd, CIlow, CIhigh = OR(ct.iloc[1,1], ct.iloc[1,0], ct.iloc[0,1], ct.iloc[0,0])
pvalue = chi2(ct.iloc[1,1], ct.iloc[1,0], ct.iloc[0,1], ct.iloc[0,0])
print('Relationship between smoking and stroke')
print('Odd ratio = ', Odd)
print('95%Confidential interval = ', [CIlow, CIhigh])
print('P-value = ', pvalue)



# create scatter plot of relationships between blood glucose and bmi
bs_bmi = df[['gender', 'age', 'avg_glucose_level', 'bmi']]
bs_bmi = bs_bmi[bs_bmi['bmi'] > 0]
print(bs_bmi)

colors = []
for index, rows in bs_bmi.iterrows() : 
    if rows['avg_glucose_level'] < 110 :
        colors.append('green')
    elif rows['avg_glucose_level'] < 125 :
        colors.append('yellow')
    elif rows['avg_glucose_level'] < 180 :
        colors.append('darkorange')
    else :
        colors.append('red')
colors = np.array(colors)


plt.scatter(bs_bmi['bmi'], bs_bmi['avg_glucose_level'], c = colors, s = bs_bmi['age']*2, alpha = 0.5)
plt.title('Relationships between blood glucose and BMI')
plt.xlabel('BMI')
plt.ylabel('Blood glucose')
plt.show()