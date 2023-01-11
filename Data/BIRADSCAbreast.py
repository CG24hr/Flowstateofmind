# ref : data.world : Mammographic Mass
# BI-RADS assessment: 0 to 6 (ordinal)
# Age: patient's age in years (continuous)
# Shape (categorical):
    #round=1
    #oval=2
    #lobular=3
    #irregular=4
# Margin (categorical):
    #circumscribed=1
    #microlobulated=2
    #obscured=3
    #ill-defined=4
    #spiculated=5
# Density (ordinal):
    #high=1
    #iso=2
    #low=3
    #fat-containing=4
# Severity: benign=0 or malignant=1 (binominal)

# Positive predictive value of BIRADS 4+ (สมมติให้ BIRADS4-6 = pos, BIRADS1-3 = neg)
# Sensitivity of Mammogram
# 95% Confidential interval & Chi-square test

import numpy as np 
import pandas as pd 
import scipy.stats as stats
import matplotlib.pyplot as plt
df = pd.read_csv('D:\\Users\\Desktop\\Python code\\GitHub\\Flowstateofmind\\Data\\csv\\mammogram&CAbreast.csv')

ID = np.arange(1,len(df.index)+1)
df.index = ID
print(df)

# clear unknown '?' data
df_clear = df[(df['Score'] != '?') & (df['Age'] != '?') & (df['Shape'] != '?') & (df['Margin'] != '?') & (df['Density'] != '?') & (df['Malignant'] != '?')]
print(df_clear)

type = df_clear['Malignant'].value_counts()
tumor = np.array(['Benign', 'Malignancy'])
type.index = tumor
print('Benign vs Malignancy')
print(type)

BIRADS = df_clear['Score'].value_counts()
print('BIRADS score')
BIRADS = BIRADS.sort_index()
print(BIRADS)

# change values in column ['Age'] from str to int
df_clear['Age'] = df_clear['Age'].apply(lambda x : int(x))


def distribution(column) : 
    import scipy.stats 
    statistic, pvalue = scipy.stats.shapiro(column)
    return statistic, pvalue

age_distribute = df_clear[['Age']].agg(distribution)
index_age_distribute = np.array(['statistic', 'p-value'])
age_distribute.index = index_age_distribute
print(age_distribute)
if age_distribute.loc['p-value','Age'] >= 0.05 :
    print('Mean age : ', df_clear['Age'].mean(), 'The age data of patients has a normal distribution')
else :
    print('Median age : ', df_clear['Age'].median(), 'The age data of patients does not have a normal distribution')

# create new dataframe

df_clear_relation= df_clear[['Score', 'Malignant']]
print(df_clear_relation)

test = []
for index, rows in df_clear_relation.iterrows() : 
    if int(rows['Score']) >= 4 :
        test.append('Positive')
    else :
        test.append('Negative')
test = np.array(test)

df_clear_relation['Test'] = test
print(df_clear_relation)


relations = pd.crosstab(df_clear_relation['Test'], df_clear_relation['Malignant'], margins = True)
print(relations)

def dxtest (a, b, c, d) : 
    ppv = a/(a+b)
    npv = d/(c+d)
    sensitivity = a/(a+c)
    specificity = d /(b+d)
    return ppv, npv, sensitivity, specificity

ppv, npv, sensitivity, specificity = dxtest(relations.iloc[1,1], relations.iloc[1,0], relations.iloc[0,1], relations.iloc[0,0])
print('Positive predictive value of this test : ', ppv)
print('Sensitivity of this test : ', sensitivity)