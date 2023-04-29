import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stat
import statsmodels.api as sm
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
import math


# step by step exploratory data  
# descriptive study
# data visualization
# survival analysis
# clinical statistics
# predict 1 year mortality by linear regression
  
# data exploratory 
CAbreast = pd.read_csv('D:\\Users\\Desktop\\Python code\\GitHub\\Flowstateofmind\\Data\\csv\\breastcancer.csv')
print(CAbreast.columns)
print(CAbreast)
print(CAbreast.dtypes)
CAbreast = CAbreast.rename(columns = {'Reginol Node Positive' : 'Regional Node Positive', '6th Stage' : 'Staging'})


oneyear_mortal = []
for index, rows in CAbreast.iterrows() : 
    if rows['Survival Months'] <= 12 and rows['Status'] == 'Dead' : 
        oneyear_mortal.append(1)
    else : 
        oneyear_mortal.append(0)
oneyear_mortal = np.array(oneyear_mortal)
CAbreast['1 Year mortality'] = oneyear_mortal

Mainstage = []
for index, rows in CAbreast.iterrows() : 
    if rows['Staging'] == 'IIA' or  rows['Staging'] == 'IIB': 
        Mainstage.append('II')
    else : 
        Mainstage.append('III')
Mainstage = np.array(Mainstage)
CAbreast['Mainstage'] = Mainstage

CAbreast['Percent of Positive Regional Node'] = (CAbreast.loc[:, 'Regional Node Positive'] / CAbreast.loc[:, 'Regional Node Examined']) * 100

print(CAbreast)

# descriptive
Avg_survival = CAbreast[CAbreast['Status'] == 'Dead']['Survival Months'].mean()
print('Average survival time of Dead patients who had breast cancer is', round(Avg_survival, 0), 'months.')

mortality_table = pd.pivot_table(values = 'Survival Months', index = 'Status', columns = '1 Year mortality', data = CAbreast, aggfunc = [np.mean])
mortality_table = mortality_table.fillna(0)
mortality_table = mortality_table.sort_index(axis = 0, ascending = False)
mortality_table = mortality_table.sort_index(axis = 1, ascending = False)

mortality_group = CAbreast.groupby(['Status', '1 Year mortality'])['Survival Months'].agg(np.mean)
mortality_group = mortality_group.sort_index(axis = 0, ascending = False)

print('Average survival time of CA breast patients.')
print(mortality_table)
print(mortality_group)

differentiate = CAbreast['differentiate'].value_counts()
print('CA breast characteristics in this data :')
print(differentiate)

staging = CAbreast['Staging'].value_counts()
print('Stage of CA breast in this data :')
print(staging)

mainstage_survival = CAbreast.groupby('Mainstage')['Survival Months'].describe()
print('Survival time of each stage.')
print(mainstage_survival)

node_stage = pd.pivot_table(values = ['Regional Node Examined', 'Regional Node Positive'], index = 'Staging', data = CAbreast, aggfunc = [np.mean])
node_stage['Percent of Positive Regional Node'] = (node_stage.iloc[:,1] / node_stage.iloc[:, 0]) * 100
node_stage = node_stage.reset_index()
print(node_stage)

# visualization : 
sns.set_style('whitegrid')
my_palette1 = sns.color_palette("magma")

    # Compare Survival months between Stage II and III.
sns.histplot(x = 'Survival Months', data = CAbreast[CAbreast['Status'] == 'Dead'], hue = 'Mainstage', multiple = 'stack', palette = my_palette1)
plt.title('Average survival time of stage III compared with stage II CA breast.')
plt.axvline(x = mainstage_survival.loc['II', '50%'], linestyle = 'dashed', color = 'purple', label = 'Stage II Median survival time')
plt.axvline(x = mainstage_survival.loc['III', '50%'], linestyle = 'dashed', color = 'violet', label = 'Stage III Median survival time')
plt.text(mainstage_survival.loc['II', '50%'], 70, s = 'Stage II Median survival time')
plt.text(mainstage_survival.loc['III', '50%'], 50, s = 'Stage III Median survival time')
plt.show()

sns.histplot(x = 'Age', data = CAbreast, hue = 'Mainstage', multiple = 'stack', palette = my_palette1)
plt.axvline(x = CAbreast[CAbreast['Mainstage'] == 'II']['Age'].median(), linestyle = 'dashed', color = 'darkgrey', label = 'Stage II Median Age')
plt.axvline(x = CAbreast[CAbreast['Mainstage'] == 'III']['Age'].median(), linestyle = 'dashed', color = 'darkgrey', label = 'Stage III Median Age')
plt.text(CAbreast[CAbreast['Mainstage'] == 'II']['Age'].median(), 300, s = 'Stage II Median Age is equal to Stage III Median age')
plt.title('Age distribution')
plt.show()

sns.set_style('whitegrid')
my_palette1 = sns.color_palette("magma")
g = sns.catplot(x = 'Staging', y = 'Percent of Positive Regional Node', data = node_stage, kind = 'bar', palette = my_palette1)
g.fig.suptitle('Average Percent of Positive Regional Node in each stage.')
g.set(xlabel = 'Stage', ylabel = 'Percent of positive node from examination')
plt.show()

g = sns.catplot(x = 'Staging', y = 'Tumor Size', data = CAbreast, kind = 'box', palette = my_palette1, whis = [5, 95], sym = '', order = ['IIA','IIB','IIIA','IIIB','IIIC'])
g.fig.suptitle('Tumor size and Staging.')
g.set(xlabel = 'Stage', ylabel = 'Tumor size')
plt.show()

# clinical statistics : difference of survival months between between stage II and stage III 
    # wilcoxon rank sum 

stat, pvalue = stat.ranksums(CAbreast[CAbreast['Mainstage'] == 'II'].loc[: , 'Survival Months'], CAbreast[CAbreast['Mainstage'] == 'III'].loc[: , 'Survival Months'])
print('There is significant difference of survival time between CA breast stage II and III patients. P-value : ', pvalue)


# predict 1 year mortality
# display model by statmodels.api
X = CAbreast[['Age', 'Tumor Size', 'Regional Node Positive']]
Y = CAbreast['1 Year mortality']

X = sm.add_constant(X)
model = sm.Logit(Y, X)
result = model.fit()
result = result.summary2()
print(result)

# train and predict with scikitlearn
X = CAbreast[['Age', 'Tumor Size', 'Regional Node Positive']]
Y = CAbreast['1 Year mortality']
X_train, X_test, Y_train, Y_test = train_test_split(X.values, Y.values, test_size = 0.2, random_state = 123)
model = LogisticRegression()
model.fit(X_train, Y_train)
Y_predict = model.predict(X_test)
accuracy = accuracy_score(Y_test, Y_predict) 
print('Accuracy :', accuracy)
Y_newpatient = model.predict(np.array([[60, 100, 0]]))
print('If patient is 60 years old and tumor size is 100 cm2, but the patient does not have regional node metastasis, The one year mortality is ', Y_newpatient, 'None.')