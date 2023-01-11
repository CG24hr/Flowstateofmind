# manipulate dataframe practice
# crosstable
# odd ratio, p-values, 95%CI of relationships between HIV infection and Monkey pox
# clinical diagnostic test for Genitorectal lesions compared with monkeypox PCR

class study :
    def diagnostic (a,b,c,d) : 
        sensitivity = a/(a+c)
        specificity = d/(b+d)
        ppv = a/(a+b)
        npv = d/(c+d)
        return sensitivity, specificity, ppv, npv

    def OR (a, b, c, d) : 
        import scipy.stats as stats
        import math
        odd = a/b * d/c
        CIlow, CIhigh = stats.norm.interval(0.95, odd, math.sqrt((1/a) + (1/b) + (1/c) + (1/d)))
        table = np.array([[a,b], [c,d]])
        chi, pvalue, dof, expected = stats.chi2_contingency(table)
        return odd, CIlow, CIhigh, pvalue

   

import pandas as pd
import numpy as np
mp = pd.read_csv('D:\\Users\\Desktop\\Python code\\GitHub\\Flowstateofmind\\Data\\csv\\Monkeypox.csv')
mp = mp.set_index('Patient_ID')
print(mp)

data = mp.columns
print(data)

mp = mp.rename(columns = {'MonkeyPox':'MonkeypoxPCR', 'Penile lesions':'Penile Lesions'})
print(mp)

mp_sortPCR = mp.sort_values('MonkeypoxPCR', ascending = False)
print(mp_sortPCR)

Genitorectal = []
for index, rows in mp.iterrows() : 
    if rows['Rectal Lesions'] == True or rows['Penile Lesions'] == True :
        Genitorectal.append(True)
    else :
        Genitorectal.append(False)
Genitorectal = np.array(Genitorectal)
mp['Genitorectal Lesions'] = Genitorectal
print(mp)

test = mp.loc[:, ['Genitorectal Lesions', 'MonkeypoxPCR']]
print(test)

test_cross = pd.crosstab(test['Genitorectal Lesions'], test['MonkeypoxPCR'])
test_cross = test_cross.sort_index(axis = 0, ascending = False)
test_cross = test_cross.sort_index(axis = 1, ascending = False)
print(test_cross)


sens, spec, ppv, npv = study.diagnostic(test_cross.iloc[0, 0], test_cross.iloc[0, 1], test_cross.iloc[1, 0], test_cross.iloc[1, 1])
print('Sensitivity of Genitorectal lesion : ', sens * 100, ' %')
print('Specificity of Genitorectal lesion : ', spec * 100, ' %')
print('Positive predictive value of Genitorectal lesion : ', ppv * 100, ' %')
print('Negative predictive value of Genitorectal lesion : ', npv * 100, ' %')

HIV_pox = pd.crosstab(mp['HIV'], mp['MonkeypoxPCR'])
HIV_pox = HIV_pox.sort_index(axis = 0, ascending = False)
HIV_pox = HIV_pox.sort_index(axis = 1, ascending = False)
print(HIV_pox)

odd, CIlow, CIhigh, pvalue = study.OR(HIV_pox.iloc[0,0], HIV_pox.iloc[0, 1], HIV_pox.iloc[1, 0], HIV_pox.iloc[1, 1])
print('Our study result shows HIV patients have more risk for monkeypox infection compared with non-HIV patients.')
print('Odd ratio :', round(odd, 2))
print('95% Confidential interval : ', [round(CIlow, 2), round(CIhigh, 2)])
print('P-value : ', round(pvalue, 2))

# Dataframe manipulation practice

Lesions = mp.groupby(['MonkeypoxPCR', 'HIV'])[['Genitorectal Lesions', 'Systemic Illness']].agg(np.count_nonzero)
Lesions = Lesions.sort_index(axis = 0, ascending = False)
total = mp['MonkeypoxPCR'].value_counts()
print(Lesions)
print('Total monkeypox patients in this study = ')
print(total)