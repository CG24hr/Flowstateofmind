# Project : CTS diagnosis by EDx, Correlation study, Cross-sectional study. screening test
# data : age, sex, height, weight, symptoms, signs, underlying[DM, RA] more than 5 years
    # calcuate BMI
# Combined sensory index (CSI) : 3 tests for peak latency(ms), median latency - reference latency
    # median-ulnar ring finger latency : >= 0.4
    # median-radial thumb latency : >= 0.5
    # median-ulnar palm latency : >= 0.3
    # csi : summary of 3 tests >= 0.9 ms 
# CTS : True, if csi >= 0.9 / False, if csi < 0.9 
# cross-sectional study : RA and CTS
# screening test : provocative signs vs gold standard(CSI from Edx)



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import math
import random

class study :
    def distribution(self, data) : 
        self.stat, self.pvalue = stats.shapiro(data) 
        return self.pvalue 

    def OR (self, a, b, c, d) : 
        self.OR = (a/b) / (c/d)
        self.CI_low, self.CI_high = stats.norm.interval(0.95, self.OR, math.sqrt((1/a) + (1/b) + (1/c) + (1/d)))
        self.chi2_table = np.array([[a, b], [c, d]])
        self.chi, self.pvalue, self.dof, self.expect = stats.chi2_contingency(self.chi2_table)
        return self.OR, self.CI_low, self.CI_high, self.pvalue

n = int(input("Sample size : "))
age = np.round(np.random.normal(50, 10, n), 0)
sex = np.random.choice(["M", "F"], p = [0.5, 0.5], size = n)

height = []
for i in sex :
    if i == "M" :
        height.append(random.randint(165,180))
    elif i == "F" :
        height.append(random.randint(155,170))
height = np.array(height)

weight = []
for i in sex : 
    if i == "M" :
        weight.append(random.randint(60, 100))
    elif i == "F" : 
        weight.append(random.randint(40, 80))
weight = np.array(weight)

BMI = np.round(weight / (height / 100) **2, 2)

# symptoms : 0 = False, 1 = True
numbness = np.random.choice([0, 1], p = [0.5, 0.5], size = n)
weakness = np.random.choice([0, 1], p = [0.5, 0.5], size = n)
pain = np.random.choice([0, 1], p = [0.5, 0.5], size = n)

# signs : 0 = False, 1 = True
tinel = np.random.choice([0, 1], p = [0.5, 0.5], size = n)
phalen = np.random.choice([0, 1], p = [0.5, 0.5], size = n)

# underlying : DM,Rheumatoid arthritis,None of these
DM = np.random.choice([0, 1], p = [0.4, 0.6], size = n)
RA = np.random.choice([0, 1], p = [0.4, 0.6], size = n)

dict = {"Age" : age,
        "Gender" : sex, 
        "Height" : height,
        "Weight" : weight,
        "BMI" : BMI,
        "Numbness" : numbness,
        "Weakness" : weakness,
        "Pain" : pain, 
        "Tinel's sign" : tinel,
        "Phalen's sign" : phalen,
        'DM' : DM,
        'RA' : RA
        }

data = pd.DataFrame(dict)
print(data)

# Simulate difference of sensory latency from 3 tests 
    # median-ulnar ring finger latency : >= 0.4 , 'MU_ring'
    # median-radial thumb latency : >= 0.5 , 'MR_thumb'
    # median-ulnar palm latency : >= 0.3 , 'MU_palm'
    # csi : summary of 3 tests >= 0.9 ms 

MU_ring = np.round(np.random.normal(0.3, 0.15, n), 2)
MR_thumb = np.round(np.random.normal(0.4, 0.2, n), 2)
MU_palm = np.round(np.random.normal(0.2, 0.1, n), 2)

data['MU_ring'] = MU_ring
data['MR_thumb'] = MR_thumb
data['MU_palm'] = MU_palm
data['csi'] = data['MU_ring'] + data['MR_thumb'] + data['MU_palm']

print(data)

# diagose CTS

CTS = []
for index, rows in data.iterrows() : 
    if rows['csi'] >= 0.9 : 
        CTS.append(1) 
    else :
        CTS.append(0)
data['CTS'] = np.array(CTS)

print(data)

cts = data[data['CTS'] == 1]
non_cts = data[data['CTS'] == 0]

print(cts)
print(non_cts)

# descriptive : distribution of age between CTS and non-CTS
avg_age = data.groupby('CTS')[['Age', 'BMI']].mean()
print(avg_age)

gender_count = data.groupby('CTS')['Gender'].value_counts()
print(gender_count)

descriptive_ncs =  data[['MU_ring', 'MR_thumb', 'MU_palm', 'csi']].describe()
print(descriptive_ncs)

data[data['CTS'] == 1]['Age'].hist(bins = 10, alpha = 0.75, label = 'CTS group')
data[data['CTS'] == 0]['Age'].hist(bins = 10, alpha = 0.75, label = 'non-CTS group')
plt.title('Average age between CTS and non-CTS group.')
plt.axvline(avg_age.iloc[1, 0], color = 'navy', linestyle = 'dashed', label = 'Mean age of CTS group')
plt.axvline(avg_age.iloc[0, 0], color = 'red', linestyle = 'dashed',label = 'Mean age of non-CTS group')
plt.legend()
plt.show()

data[data['CTS'] == 1]['BMI'].hist(bins = 10, alpha = 0.75, label = 'CTS group')
data[data['CTS'] == 0]['BMI'].hist(bins = 10, alpha = 0.75, label = 'non-CTS group')
plt.title('Average BMI between CTS and non-CTS group.')
plt.axvline(avg_age.iloc[1, 1], color = 'navy', linestyle = 'dashed', label = 'Mean BMI of CTS group')
plt.axvline(avg_age.iloc[0, 1], color = 'red', linestyle = 'dashed',label = 'Mean BMI of non-CTS group')
plt.legend()
plt.show()

csi_underlying = data.pivot_table(values = 'csi', index = 'CTS', columns = ['DM', 'RA'], aggfunc = np.mean, margins = False, fill_value = 0)
print('Average combined sensory index in each groups')
print(csi_underlying)

# cross-sectional study : RA and CTS
RA_CTS = pd.crosstab(data['RA'], data['CTS'])
RA_CTS = RA_CTS.sort_index(axis = 0, ascending = False)
RA_CTS = RA_CTS.sort_index(axis = 1, ascending = False)
print(RA_CTS)

cross_sec = study()
odd, CI_low, CI_high, pvalue = cross_sec.OR(RA_CTS.iloc[0,0], RA_CTS.iloc[0,1], RA_CTS.iloc[1,0], RA_CTS.iloc[1,1])
print('Odd ratio of Rheumatoid arthritis in CTS group compared to non-CTS group.')
print('Odd ratio : ', round(odd, 2))
print('95%CI[{},{}]'.format(round(CI_low, 2), round(CI_high, 2)))
print('P-value = ', round(pvalue, 2))


# screening test
phalen = pd.crosstab(data["Phalen's sign"], data["CTS"])
phalen = phalen.sort_index(axis = 0, ascending = False)
phalen = phalen.sort_index(axis = 1, ascending = False)
print(phalen)

sensitivity = phalen.iloc[0, 0] / (phalen.iloc[0, 0] + phalen.iloc[0, 1])
specificity = phalen.iloc[1, 1] / (phalen.iloc[1, 1] + phalen.iloc[1, 0])

print("Sensitivity of Phalen's test = {}".format(round(sensitivity*100), 2), '%')
print("Specificity of Phalen's test = {}".format(round(specificity*100), 2), '%')