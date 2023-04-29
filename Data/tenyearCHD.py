import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import math
import statsmodels.api as sm
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.preprocessing import LabelEncoder


CHD = pd.read_csv('D:\\Users\\Desktop\\Python code\\GitHub\\Flowstateofmind\\Data\\csv\\tenyearsCHD.csv')

# Explore data 
print(CHD.columns)
print('Sample size', len(CHD.index))
print(CHD.isna().sum())
CHD = CHD.dropna()
print(CHD.shape)
print(CHD.dtypes)
print(CHD)


# Descriptive study 
gender_age = CHD.groupby('male')['age'].mean()
gender_age = gender_age.sort_index(axis = 0, ascending = False)
print('Average age comparison between gender.')
print(gender_age)

gender_smoke = pd.crosstab(CHD['male'], CHD['currentSmoker'])
gender_smoke = gender_smoke.sort_index(axis = 0, ascending = False)
gender_smoke = gender_smoke.sort_index(axis = 1, ascending = False)
print('Current Smoker')
print(gender_smoke)

smoke_HT = CHD.groupby(['prevalentStroke', 'prevalentHT'])['cigsPerDay'].agg(np.mean)
smoke_HT = smoke_HT.sort_index(ascending = False)
print('Average ciggarettes smoking per day comparison between Old CVA and HT groups.')
print(smoke_HT)


totalChol_stroke = CHD.groupby('prevalentStroke')['totChol'].describe()
totalChol_stroke = totalChol_stroke.sort_index(ascending = False)
print('Comparison of Total serum cholesterol between Old CVA and non-Old CVA groups.')
print(totalChol_stroke)

FBS_stroke = CHD.groupby('prevalentStroke')['FBS'].describe()
FBS_stroke = FBS_stroke.sort_index(ascending = False)
print('Comparison of FBS between Old CVA and non-Old CVA groups.')
print(FBS_stroke)

bmi_ht_dm = pd.pivot_table(data = CHD, values = 'BMI', index = 'prevalentHT', columns = 'dm', aggfunc=[np.std, np.mean])
bmi_ht_dm = bmi_ht_dm.sort_index(axis = 0, ascending = False)
bmi_ht_dm = bmi_ht_dm.sort_index(axis = 1, ascending = False)
print('Average BMI comparison between DM and HT groups')
print(bmi_ht_dm)

onepack = []
for index, rows in CHD.iterrows() :
    if rows['cigsPerDay'] >= 10 : 
        onepack.append(1)
    else : 
        onepack.append(0)
onepack = np.array(onepack)
CHD['smokeonepack'] = onepack


tenyearCHD_smoke = pd.crosstab(CHD['smokeonepack'], CHD['TenYearCHD'])
tenyearCHD_smoke = tenyearCHD_smoke.sort_index(axis = 0, ascending = False)
tenyearCHD_smoke = tenyearCHD_smoke.sort_index(axis = 1, ascending = False)
print('Ten pack year smoker and Ten years coronary heart disease incidence')
print(tenyearCHD_smoke)

tenyearCHD_HT = pd.crosstab(CHD['prevalentHT'], CHD['TenYearCHD'])
tenyearCHD_HT = tenyearCHD_HT.sort_index(axis = 0, ascending = False)
tenyearCHD_HT = tenyearCHD_HT.sort_index(axis = 1, ascending = False)
print('Hypertension and Ten years coronary heart disease incidence')
print(tenyearCHD_HT)


print()
print()
print('Clinical Statistics part')
print()
# Clinical statistics : 
    # null hypothesis : Male commonly smokes ciggarettes more than female significantly. (chi-square test, gender_smoke cross table)
gender_smoke = gender_smoke.values
chi, pvalue_gender_smoke, dof, expected = stats.chi2_contingency(gender_smoke)
print('Number of male smokers is significantly more than female smokers. Pvalue : {}'.format(round(pvalue_gender_smoke, 2)))
    # correlation between BMI and Systolic BP, BMI 
corr, pvalue_bmi_sbp = stats.pearsonr(CHD['BMI'], CHD['sysBP'])
print('There is significant correlation between BMI and systolic blood pressure.')
print('Correlation coefficient = ', round(corr, 2))
print('p-value = ', round(pvalue_bmi_sbp, 2))
    # Ten years CHD and current smoker : case control -> calculate OR, 95% CI and p-value
tenyearCHD_smoke = tenyearCHD_smoke.values
a = tenyearCHD_smoke[0, 0]
b = tenyearCHD_smoke[0, 1]
c = tenyearCHD_smoke[1, 0]
d = tenyearCHD_smoke[1, 1]
Odd_smoke_CHD = (a / b) / (c / d)
CI_low, CI_high = stats.norm.interval(0.95, Odd_smoke_CHD, math.sqrt((1/a) + (1/b) + (1/c) + (1/d)))
chi, pvalue_CHD_smoke, dof, expect = stats.chi2_contingency(tenyearCHD_smoke)
print('There is significant increasing of Ten year coronary heart disease incidence in ten pack year smoker group.')
print('Odd ratio : ', round(Odd_smoke_CHD, 2), '95%CI',[round(CI_low, 2), round(CI_high, 2)])
print('P-value : ', round(pvalue_CHD_smoke, 2))

    # Ten years CHD and HT : case control -> calculate OR, 95% CI and p-value
tenyearCHD_HT = tenyearCHD_HT.values
a = tenyearCHD_HT[0, 0]
b = tenyearCHD_HT[0, 1]
c = tenyearCHD_HT[1, 0]
d = tenyearCHD_HT[1, 1]
Odd_HT_CHD = (a / b) / (c / d)
CI_low, CI_high = stats.norm.interval(0.95, Odd_HT_CHD, math.sqrt((1/a) + (1/b) + (1/c) + (1/d)))
chi, pvalue_CHD_HT, dof, expect = stats.chi2_contingency(tenyearCHD_HT)
print('There is significant increasing of Ten year coronary heart disease incidence in Hypetension group.')
print('Odd ratio : ', round(Odd_HT_CHD, 2), '95%CI',[round(CI_low, 2), round(CI_high, 2)])
print('P-value : ', round(pvalue_CHD_HT, 2))

    # Null hypothesis : there is no significantly different total serum cholesterol between CHD and non-CHD group
stat, pvalue_chol_CHD = stats.ttest_ind(CHD[CHD['TenYearCHD'] == 1]['totChol'], CHD[CHD['TenYearCHD'] == 0]['totChol'])
print('Total serum cholesterol in coronary heary disease group is significantly higher than non-coronary heart disease group. p-value : ', round(pvalue_chol_CHD, 2))

    # Null hypothesis : there is no significantly different number of ciggarette per day between CHD and non-CHD group
stat, pvalue_cig_CHD = stats.mannwhitneyu(CHD[CHD['TenYearCHD'] == 1]['cigsPerDay'], CHD[CHD['TenYearCHD'] == 0]['cigsPerDay'])
print('Number of ciggarette per day in coronary heary disease group is significantly higher than non-coronary heart disease group. p-value : ', round(pvalue_cig_CHD, 2))


# Data visualization 
sns.set_style('whitegrid')
my_palette = sns.cubehelix_palette(2, start = 0, dark = 0.30, light = 0.65)

sns.catplot(x = 'currentSmoker', data = CHD, hue = 'male', kind = 'count', palette = my_palette)
plt.title('Number of current smokers in male and female groups.')
plt.show()

sns.relplot(x = 'BMI', y = 'sysBP', data = CHD[CHD['dm'] == 1], alpha = 1.0, hue = 'prevalentHT', palette = my_palette)
plt.title('Relationship between BMI and systolic blood pressure in DM group.')
plt.show()


sns.catplot(x = 'smokeonepack', y = 'TenYearCHD', data = CHD, hue = 'prevalentHT', kind = 'point', palette = my_palette)
plt.title('Incidence of ten years coronary heart disease comparison between 10-packs-year smoker and less.')
plt.xlabel('Smoke 10-packs-year')
plt.ylabel('Incidence of coronary heart disease.')
plt.show()

sns.histplot(x = 'totChol', data = CHD, hue = 'TenYearCHD', palette = my_palette, bins = 40)
plt.title('Total serum cholesterol level comparison between CHD and non-CHD group.')
plt.xlabel('Total cholesterol')
plt.axvline(CHD[CHD['TenYearCHD'] == 1]['totChol'].mean(), label = 'Mean total cholesterol in CHD group', linestyle = 'dashed', color = 'purple')
plt.axvline(CHD[CHD['TenYearCHD'] == 0]['totChol'].mean(), label = 'Mean total cholesterol in non-CHD group', linestyle = 'dashed', color = 'magenta')
plt.text(CHD[CHD['TenYearCHD'] == 1]['totChol'].mean()+2, 50, s = 'Mean total cholesterol in CHD group', color = 'purple')
plt.text(CHD[CHD['TenYearCHD'] == 0]['totChol'].mean()+2, 200, s = 'Mean total cholesterol in non-CHD group', color = 'magenta')
plt.show()

sns.catplot(x = 'TenYearCHD', y = 'cigsPerDay', data = CHD[CHD['prevalentHT'] == 0], kind = 'box', palette = my_palette, sym = ' ')
plt.title('Number of cigarettes per day and ten years coronary heart disease')
plt.xlabel('Ten years CHD')
plt.ylabel('Cigarettes per day')
plt.show()


# Logistic regression : predict ten years CHD 
    # show model by statsmodels.api
X = CHD[['male', 'age', 'currentSmoker', 'cigsPerDay', 'prevalentHT', 'dm', 'totChol', 'BMI', 'HR']]
Y = CHD['TenYearCHD']
X = sm.add_constant(X)
model = sm.Logit(Y, X)
result = model.fit()
result = result.summary2()
print(result)
    # train data by scikitlearn
X = CHD[['male', 'age', 'cigsPerDay', 'prevalentHT', 'dm', 'totChol', 'BMI']]
Y = CHD['TenYearCHD']
X_train, X_test, Y_train, Y_test = train_test_split(X.values, Y.values, test_size = 0.2, random_state = 123)
model = LogisticRegression()
model.fit(X_train, Y_train)
        # test accuracy of model
Y_predict_test = model.predict(X_test)
confusionMatrix = confusion_matrix(Y_test, Y_predict_test)
accuracy = accuracy_score(Y_test, Y_predict_test, )
print(confusionMatrix)
print('Accuracy score of this logistic regression model : ', accuracy)

input = np.array([[1, 60, 10, 1, 1, 0, 35]])
Y_predict_new = model.predict(input)
print('Male, 60 years, smoking 1 pack-year, HT, DM, non-hypercholesterolemia, BMI 35')
print('Ten year coronary heart disease = ', Y_predict_new)