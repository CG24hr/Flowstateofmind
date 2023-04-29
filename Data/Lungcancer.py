# reference : https://www.kaggle.com/code/mdsajidanamifti/lung-cancer-prediction-and-visualization#Decision-Tree


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stat
import pingouin as pg
import statsmodels.api as sm
from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, accuracy_score


# explore data
lungCA = pd.read_csv('D:\\Users\\Desktop\\Python code\\GitHub\\Flowstateofmind\\Data\\csv\\Lungcancer.csv')
print(lungCA.columns)
print(lungCA.isna().sum())

lungCA = lungCA.dropna()
print(lungCA)
print('Sample size : ', len(lungCA.index))

stage_dict = {'High':'1', 'Medium' : '2', 'Low' : '3'}
lungCA['Level'] = lungCA['Level'].replace(stage_dict)
lungCA = lungCA.rename(columns = {'Level' : 'Types'})


# descriptive study : 
Age_cancer = lungCA.groupby('Types')['Age'].mean()
Age_cancer = Age_cancer.reset_index()
Age_cancer = Age_cancer.sort_values('Age', ascending = False )
Age_cancer = Age_cancer.set_index('Types')
print('Mean Age in different types of lung cancer.')
print(Age_cancer)

symptoms = lungCA.groupby('Types')[['Chest Pain', 'Coughing of Blood', 'Fatigue', 'Weight Loss']].agg(np.mean)
print('Severity of symptoms in different lung cancer types.')
print(symptoms)

Types = lungCA['Types'].value_counts(normalize = True)
print('Ratios of different lung cancer types in this study')
print(Types)

smoking_types = lungCA[['Smoking', 'Passive Smoker', 'Types']]
smoking_types = smoking_types.melt(id_vars='Types', var_name = 'Smoke/Passive', value_name = 'packs/year')
smoking_types = smoking_types.sort_values('Types', ascending = True)
print(smoking_types) # สร้าง dataframe นี้เพื่อไป plot histogram โดยใช้ hue เป็น 'Smoke/Passive'

smoking_types_median = lungCA.groupby('Types')[['Smoking', 'Passive Smoker']].median()
print(smoking_types_median)


# clinical statistics : 
    # chi-square : 
        # H0 : There is no relationship between genetic risk and Types of lung cancer 
print('Relationships between genetic risks and lung cancer Types.')
genetic_types = lungCA.groupby('Genetic Risk')['Types'].value_counts(normalize = True)
print(genetic_types)
genetic_types = genetic_types.unstack()
print(genetic_types)
genetic_types_crosstab = pd.crosstab(lungCA['Genetic Risk'], lungCA['Types'])
print(genetic_types_crosstab)
chi2, pvalue_genetic_types, dof, expected = stat.chi2_contingency(genetic_types_crosstab)
print('There is relationships between genetic risks and types of lung cancer.')
print('p-value : ', pvalue_genetic_types)
        # H0 : There is no relationship between types of chronic lung diseases and types of lung cancer 
print('Relationships between chronic lung diseases and lung cancer Types.')
chronicLung_types = lungCA.groupby('chronic Lung Disease')['Types'].value_counts(normalize = True)
chronicLung_types = chronicLung_types.unstack()
print(chronicLung_types)
chronicLung_types_crosstab = pd.crosstab(lungCA['chronic Lung Disease'], lungCA['Types'])
print(chronicLung_types_crosstab)
chi2, pvalue_chronicLung_types, dof, expected = stat.chi2_contingency(chronicLung_types_crosstab)
print('There is relationships between chronic lung diseases and types of lung cancer.')
print('p-value : ', pvalue_chronicLung_types)

    # t-test : 
        # H0 : there is no difference of age between lung cancer types
anova_age_types = pg.anova(data = lungCA, dv = 'Age', between = 'Types')
print('There are differences of ages between groups of lung cancer types')
print(anova_age_types)
        # H0 : There is no difference of lung cancer risk between smoker and passive smoker
stats, pvalue_smoking = stat.wilcoxon(smoking_types[smoking_types['Smoke/Passive'] == 'Smoking']['packs/year'], smoking_types[smoking_types['Smoke/Passive'] == 'Passive Smoker']['packs/year'])
print('There is difference between packs-year of smoking related with lung cancer between smokers and passive smokers')
print('p-value : ', pvalue_smoking)


# data visualization : 
sns.set_style('whitegrid')
my_palette = sns.color_palette(['navy', 'cornflowerblue', 'lavender'])
    # age distribution of each types
sns.kdeplot(data = lungCA, x = 'Age', hue = 'Types', palette = my_palette)
plt.axvline(x = Age_cancer.loc['1', 'Age'], linestyle = 'dashed', color = 'lightskyblue')
plt.axvline(x = Age_cancer.loc['2', 'Age'], linestyle = 'dashed', color = 'cornflowerblue')
plt.axvline(x = Age_cancer.loc['3', 'Age'], linestyle = 'dashed', color = 'navy')
plt.text(Age_cancer.loc['1', 'Age']+0.2, 250, s = 'Mean age of types I', color = 'lightskyblue')
plt.text(Age_cancer.loc['2', 'Age']+0.2, 200, s = 'Mean age of types II', color = 'cornflowerblue')
plt.text(Age_cancer.loc['3', 'Age']+0.2, 150, s = 'Mean age of types III', color = 'navy')
plt.xlabel('Age')
plt.ylabel('Count')
plt.title('Age and lung cancer types.')
plt.legend()
    # smoker and passive smoker in each lung cancer type
sns.catplot(data = smoking_types, x = 'Types', y = 'packs/year', hue = 'Smoke/Passive', kind = 'box', whis = [0, 100], sym = '', palette = my_palette)
plt.xlabel('Types')
plt.ylabel('packs/year')
plt.title('Median packs-year smoking between smoker and passive smoker in lung cancer.')
    # air pollution vs. Smoking vs. Passive Smoker 
    # genetic risks and Types of lung cancer
genetic_types.plot(kind = 'bar', stacked = True, color = ['lavender', 'cornflowerblue', 'navy'])
plt.title('Relationships between genetic risks and types of lung cancer.')
plt.ylabel('Ratios')
    # Chronic lung Disease and Types of lung cancer (stacked bar)
chronicLung_types.plot(kind = 'bar', stacked = True, color = ['lavender', 'cornflowerblue', 'navy'])
plt.title('Relationships between chronic lung diseases and types of lung cancer.')
plt.ylabel('Ratios')
plt.show()

# decision tree
    # train data
X = lungCA[['Age', 'Gender', 'Air Pollution', 'Alcohol use', 'Genetic Risk', 'chronic Lung Disease', 'Smoking']]
Y = lungCA['Types']
X_train, X_test, Y_train, Y_test = train_test_split(X.values, Y.values, test_size = 0.2, random_state = 123)
model = DecisionTreeClassifier()
model.fit(X_train, Y_train)
    # test for accuracy
Y_predict_test = model.predict(X_test)
confusionMatrix = confusion_matrix(Y_test, Y_predict_test)
accuracy = accuracy_score(Y_test, Y_predict_test)
print('Confusion matric')
print(confusionMatrix)
print('Accuracy : ', accuracy)

    # predict
input = np.array([[40, 2, 5, 5, 5, 5, 5]])
Y_predict_new = model.predict(input)
print(Y_predict_new)