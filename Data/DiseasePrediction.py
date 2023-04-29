import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stat
import statsmodels.api as sm
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
import math

Disease = pd.read_csv('D:\\Users\\Desktop\\Python code\\GitHub\\Flowstateofmind\\Data\\csv\\diseasePrediction.csv')
Disease = Disease.rename(columns = {'Disease' : 'Disease'})
Disease = Disease.set_index('ID')
print(Disease.columns)
print(Disease)

# create OOP and method for statistic calculation
class research() :
    def diagnostic(self, array) : 
        sensitivity = array[0, 0] / (array[0, 0] + array[1, 0])
        specificity = array[1, 1] / (array[1, 1] + array[0, 1])
        ppv = array[0, 0] / (array[0, 0] + array[0, 1])
        npv = array[1, 1] / (array[1, 1] + array[1, 0])
        return sensitivity, specificity, ppv, npv
    def Oddratio(self, array) :
        import scipy.stats as stat
        a = array[0, 0]
        b = array[0, 1]
        c = array[1, 0]
        d = array[1, 1]
        odd_Exposed = a / b
        odd_nonExposed  = c / d
        oddRatio = odd_Exposed / odd_nonExposed
        CI_low, CI_high = stat.norm.interval(0.95, oddRatio, math.sqrt((1/a) + (1/b) + (1/c) + (1/d)))
        chi, pvalue, dof, expected  = stat.chi2_contingency(array)
        return oddRatio, CI_low, CI_high, pvalue



# descriptive study : patients baseline characteristics
Disease_count = Disease['Disease'].value_counts()
Disease_count = Disease_count.sort_index(ascending = False)
print('Number of participants.')
print(Disease_count)

Disease_age = Disease.groupby('Disease')['Age'].describe()
Disease_age = Disease_age.sort_index(ascending = False)
print('Baseline age between both groups')
print(Disease_age)

stat, pvalue = stat.ttest_ind(Disease[Disease['Disease'] == 'Positive']['Age'], Disease[Disease['Disease'] == 'Negative']['Age'])
print('There is significanct age difference between Disease and Non-Disease group. Pvalue :', round(pvalue, 2))




# กรณี cross sectional study : diagnostic test : PL, สมมติว่า 110 = high, นอกนั้น normal
A = Disease.loc[:, ['A', 'Disease']].sort_values('Disease', ascending = False)
baselineA = []
for index, rows in A.iterrows() : 
    if rows['A'] >= 110 :
        baselineA.append('high')
    else : 
        baselineA.append('normal')
baselineA = np.array(baselineA)
A['baselineA'] = baselineA
print(A)

A_groupbyDisease = A.groupby('Disease')['A'].describe()
A_groupbyDisease = A_groupbyDisease.sort_index(axis = 0, ascending = False)
print('serum A level between groups')
print(A_groupbyDisease)

table = pd.crosstab(A['baselineA'], A['Disease'])
table = table.sort_index(axis = 1, ascending = False)
print(table)
table_array = table.values

diagnostic_study = research()
sensitivity, specificity, ppv, npv = diagnostic_study.diagnostic(table_array)
print('Sensitivity of serum A level for Disease screening : ', round(sensitivity, 2))
print('Specificity of serum A level for Disease screening : ', round(specificity, 2))


# กรณี case control study : hypothesis testing : Null hypothesis - > There is significant elevation of serum PL in Disease group compared with Non-Disease group.
# อ้างอิงข้อมูลเดียวกับ A, A_groupbyDisease  # Odd ratios
casecontrol_table = pd.crosstab(A['Disease'], A['baselineA'])
casecontrol_table = casecontrol_table.sort_index(axis = 0, ascending = False)
print(casecontrol_table)
casecontrol_table_array = casecontrol_table.values

casecontrol = research()
Oddratio, CI_low, CI_high, pvalue_odd = casecontrol.Oddratio(casecontrol_table_array)
print('There are significant rising of serum A levels in Disease group compared with Non-Disease group.')
print('Odd ratio :', round(Oddratio, 2))
print('95%CI[{}, {}]'.format(round(CI_low, 2), round(CI_high, 2)), ' pvalue : {} '.format(round(pvalue_odd, 2)))

# Multiple logistic regression : Disease prediction , except Age
Disease['Disease'] = Disease['Disease'].replace({'Positive':1, 'Negative':0})
# statmodels for coefficient and pvalue calculation
X = Disease[['A', 'B', 'C', 'D', 'E', 'F']]
Y = Disease['Disease']

X = sm.add_constant(X)
model = sm.Logit(Y, X)
result = model.fit()
result = result.summary2()
print(result)

# scikitlearn for prediction
X = Disease[['A', 'B', 'C', 'D', 'E', 'F']]
Y = Disease['Disease']
X_train, X_test, Y_train, Y_test = train_test_split(X.values, Y.values, test_size=0.2, random_state=123) 
    # test_size = 0.2 หมายถึง random แบ่งข้อมูล 20 % ออกเป็น test set (X_test, Y_test) ให้ model ไม่เคยเห็นมาก่อน แล้วที่เหลือจะเป็น train set(X_train, Y_train) เพื่อไปเข้า model.fit()
model = LogisticRegression() # ถ้าผลลัพธ์มีมากกว่า binary variables ให้ใช้ decision tree
model.fit(X_train, Y_train)

input = np.array([140, 75, 96, 0, 40, 0.65])
new_X = pd.DataFrame([input], columns=['A', 'B', 'C', 'D', 'E', 'F'])
new_X = new_X.values.reshape(1, -1)
Y_predict_test = model.predict(X_test) # ทดสอบระบบด้วย X test
Y_predict_new = model.predict(new_X) # ลอง predict ข้อมูลจริงๆ
print('If each serum marker levels are ', X_test, ', respectively.')
print('Outcome will be : ', Y_predict_test, '(Disease)')
print('If each serum marker levels are ', input, ', respectively.')
print('Outcome will be : ', Y_predict_new, '(Disease)')
print('Accuracy:', accuracy_score(Y_test, Y_predict_test)) # ทดสอบความแม่นยำว่า Y_predict ตรงกับ Y_test ที่เราแยกข้อมูลมาตอนแรกแค่ไหน
                                                            # แต่ถ้าใช้ LinearRegression จะใช้ mean_squared_error, r2_score

# visualization
fig, ax = plt.subplots()
sns.set_style('whitegrid')
sns.histplot(x = 'Age', data = Disease, hue = 'Disease', multiple = 'stack', bins = 10, alpha = 0.5)
plt.axvline(x = Disease_age.loc['Positive', '50%'], linestyle = 'dashed', color = 'navy')
plt.axvline(x = Disease_age.loc['Negative', '50%'], linestyle = 'dashed', color = 'darkorange')
plt.text(Disease_age.loc['Positive', '50%'] + 1, 100, 'Median age for Disease', color='navy')
plt.text(Disease_age.loc['Negative', '50%'] + 1, 50, 'Median age for non-Disease', color='darkorange')
plt.title('Disease and Non-Disease Age distribution.')
plt.xlabel('Age')
plt.show()


sns.set_style('whitegrid')
sns.histplot(x = 'A', data = A, hue = 'Disease', multiple = 'layer', bins = 10, alpha = 0.5)
plt.axvline(x = A_groupbyDisease.loc['Positive', '50%'], linestyle = 'dashed', color = 'navy')
plt.axvline(x = A_groupbyDisease.loc['Negative', '50%'], linestyle = 'dashed', color = 'darkorange')
plt.text(A_groupbyDisease.loc['Positive', '50%'] + 1, 100, 'Median A for Disease', color='navy')
plt.text(A_groupbyDisease.loc['Negative', '50%'] + 1, 50, 'Median A for non-Disease', color='darkorange')
plt.title('Baseline serum A level between Disease and Non-Disease groups.')
plt.xlabel('serum A levels')
plt.show()


sns.set_style('whitegrid')
g = sns.catplot(x = 'Disease', y = 'A', data = A, kind = 'box', whis = [0, 100], order = ['Positive', 'Negative'])
g.fig.suptitle('Serum A level difference between Disease and Non-Disease groups.')
g.set(xlabel = 'Disease', ylabel = 'serum A levels')
plt.show()


# from sklearn.preprocessing import LabelEncoder
# lbl=LabelEncoder()
# df["gender"]=lbl.fit_transform(df['gender']) เปลี่ยน categorical variables ให้เป็นตัวเลข เพื่อให้ machine ไปใช้คำนวน


