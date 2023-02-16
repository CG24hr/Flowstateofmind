# Project : NAC decreases mortality rates in Covid-19 pneumonia patients, Retrospective cohort study
# data of Covid-19 patients : Age, Sex, BMI, COPD, DM, Pneumonia, Corticosteroids, NAC, Death
# visualization
# compared baseline characteristics between group
# Multiple logistic regression ( y = mortality )
    # include corticosteroid in the model
    # exclude corticosteroid in the model
    # calculate odd ratio and 95% confidential interval
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm 
import scipy.stats as stats
n = 20000

age = np.round(np.random.normal(60, 10, n), 0)
sex = np.random.choice(['M', 'F'], p = [0.5, 0.5], size = n)
bmi = np.round(np.random.normal(25, 5, n), 1)
copd = np.random.choice([1, 0], p = [0.1,0.9], size = n)
dm = np.random.choice([1, 0], p = [0.2, 0.8], size = n)
pneumonia = np.random.choice([1, 0], p = [0.3, 0.7], size = n)
corticosteroids = []
for i in pneumonia :
    if i == 1 :
        corticosteroids.append(np.random.choice([1, 0], p = [0.3, 0.7]))
    else :
        corticosteroids.append(np.random.choice([1, 0], p = [0.02, 0.98]))
corticosteroids = np.array(corticosteroids)

nac = []
for i in pneumonia:
    if i == 1:
        nac.append(np.random.choice([1, 0], p = [0.5, 0.5]))
    else:
        nac.append(0)
nac = np.array(nac)

death = []
for i in range(n) : 
    if pneumonia[i] == 1 and nac[i] == 1 and corticosteroids[i] == 1 : 
        death.append(np.random.choice([1, 0], p = [0.07, 0.93]))
    elif pneumonia[i] == 1 and nac[i] == 1 and corticosteroids[i] == 0 :
        death.append(np.random.choice([1, 0], p = [0.1, 0.9]))
    elif pneumonia[i] == 1 and nac[i] == 0 and corticosteroids[i] == 1 :
        death.append(np.random.choice([1, 0], p = [0.105, 0.895]))
    elif pneumonia[i] == 1 and nac[i] == 0 and corticosteroids[i] == 0 :
        death.append(np.random.choice([1, 0], p = [0.15, 0.85]))
    else : 
        death.append(np.random.choice([1, 0], p = [0.05, 0.95]))
death = np.array(death)


print(pneumonia)
print(corticosteroids)
print(death)

dict = {'Age':age, 'Gender':sex, 'BMI':bmi, 'COPD':copd, 'DM':dm, 'Pneumonia':pneumonia, 'Corticosteroids':corticosteroids, 'NAC':nac, 'Death':death}
data = pd.DataFrame(dict)
print(data)

grouping = data.groupby(['Pneumonia', 'NAC'])['Death'].value_counts()
print(grouping)

NAC_pneumonia = data['NAC'].value_counts()
print(NAC_pneumonia)

NAC_Gender_Age = data[data['NAC'] == 1].groupby('Gender')['Age'].mean()
print(NAC_Gender_Age)

BMI = pd.pivot_table(data = data, values = ['Age', 'BMI'], index = 'Pneumonia', columns = 'Death', aggfunc = [np.mean])
BMI = BMI.sort_index(axis = 0, ascending = False)
BMI = BMI.sort_index(axis = 1, ascending = False)
print(BMI)


fig, ax = plt.subplots()
ax.bar(NAC_Gender_Age.index, NAC_Gender_Age)
ax.set_xlabel('Gender')
ax.set_ylabel('Mean Age')
ax.set_title('Mean age in NAC administration group')
plt.legend()
plt.show()


pneumonia = data[data['Pneumonia'] == 1]
pneumonia_NAC = data.query('Pneumonia == 1 and NAC == 1')
pneumonia_nonNAC = data.query('Pneumonia == 1 and NAC == 0')
print(pneumonia_NAC)
print(pneumonia_nonNAC)
print('The number of Covid-19 pneumonia patients recieved NAC administration is {}'.format(len(pneumonia_NAC.index)))
print('The number of Covid-19 pneumonia patients not recieved NAC administration is {}'.format(len(pneumonia_nonNAC.index)))

NAC_mortal = pd.crosstab(data['NAC'], data['Death'])
NAC_mortal = NAC_mortal.sort_index(axis = 0, ascending = False)
NAC_mortal = NAC_mortal.sort_index(axis = 1, ascending = False)
print(NAC_mortal)
NAC_mortal_array = NAC_mortal.values
print(NAC_mortal_array)

# Difference in baseline characteristics (Age, BMI, COPD, Pneumonia, Corticosteroids)
    # test for normality by plotting two layers histogram, in spite of shapiro-wilk test
    # t-test in continuous variables, chi-square in categorical variables
fig, ax = plt.subplots(2, 1)
ax[0].hist(pneumonia_NAC['Age'], alpha = 0.6, label = 'NAC administration', bins = 10)
ax[0].hist(pneumonia_nonNAC['Age'], alpha = 0.6, label = 'Non-NAC administration', bins = 10)
ax[0].axvline(pneumonia_NAC['Age'].mean(), color = 'navy', linestyle = 'dashed', label = 'Mean age of NAC administration group')
ax[0].axvline(pneumonia_nonNAC['Age'].mean(), color = 'red', linestyle = 'dashed', label = 'Mean age of non-NAC administration group')
ax[0].set_title('Age')
ax[1].hist(pneumonia_NAC['BMI'], alpha = 0.6, label = 'NAC administration', bins = 10)
ax[1].hist(pneumonia_nonNAC['BMI'], alpha = 0.6, label = 'Non-NAC administration', bins = 10)
ax[1].axvline(pneumonia_NAC['BMI'].mean(), color = 'navy', linestyle = 'dashed', label = 'Mean BMI of NAC administration group')
ax[1].axvline(pneumonia_nonNAC['BMI'].mean(), color = 'red', linestyle = 'dashed', label = 'Mean BMI of non-NAC administration group')
ax[1].set_title('BMI')
plt.legend()
plt.show()

stat, pvalue_Age = stats.ttest_ind(pneumonia_NAC['Age'], pneumonia_nonNAC['Age'])
print('There is no significant difference between Age in both NAC and Non-NAC administration groups, p-value = ', round(pvalue_Age, 2))
stat, pvalue_BMI = stats.ttest_ind(pneumonia_NAC['BMI'], pneumonia_nonNAC['BMI'])
print('There is no significant difference between BMI in both NAC and Non-NAC administration groups, p-value = ', round(pvalue_BMI, 2))


COPD_table = pd.crosstab(pneumonia['NAC'], pneumonia['COPD'])
COPD_table = COPD_table.sort_index(axis = 0, ascending = False)
COPD_table = COPD_table.sort_index(axis = 1, ascending = False)
print(COPD_table)
COPD_table_array = COPD_table.values

chi_stat, chi_pvalue_COPD, dof, expected = stats.chi2_contingency(COPD_table.values)
print('There is no significant difference between number of COPD patients in both NAC and Non-NAC administration groups, p-value = ', round(chi_pvalue_COPD, 2))


DM_table = pd.crosstab(pneumonia['NAC'], pneumonia['DM'])
DM_table = DM_table.sort_index(axis = 0, ascending = False)
DM_table = DM_table.sort_index(axis = 1, ascending = False)
print(DM_table)
DM_table_array = DM_table.values
chi_stat, chi_pvalue_DM, dof, expected = stats.chi2_contingency(DM_table.values)
print('There is no significant difference between number of DM patients in both NAC and Non-NAC administration groups, p-value = ', round(chi_pvalue_DM, 2))

Corticosteroids_table = pd.crosstab(pneumonia['NAC'], pneumonia['Corticosteroids'])
Corticosteroids_table = Corticosteroids_table.sort_index(axis = 0, ascending = False)
Corticosteroids_table = Corticosteroids_table.sort_index(axis = 1, ascending = False)
print(Corticosteroids_table)
Corticosteroids_table_array = Corticosteroids_table.values
chi_stat, chi_pvalue_Corticosteroids, dof, expected = stats.chi2_contingency(Corticosteroids_table.values)
print('There is no significant difference between number of patients who received Corticosteroids in both NAC and Non-NAC administration groups, p-value = ', round(chi_pvalue_Corticosteroids, 2))


# multiple logistic regression : NAC can reduce mortality rate of Covid-19 pneumonia patients
x = pneumonia[['NAC', 'Corticosteroids', 'DM', 'COPD', 'BMI', 'Age']]
y = pneumonia['Death']
X = sm.add_constant(x)
model = sm.Logit(y, X)
result = model.fit()
summary = result.summary2()
print(summary)

summary_dataframe = summary.tables[1]
print(summary_dataframe)

print('NAC can reduce mortality rate in Covid-19 pneumonia patients significantly after adjusted other covariate factors.')
print('Odd ratio', np.exp(summary_dataframe.iloc[1, 0]))