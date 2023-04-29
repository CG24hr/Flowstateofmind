import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stat
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder


# explore data
salary = pd.read_csv('D:\\Users\\Desktop\\Python code\\GitHub\\Flowstateofmind\\Data\\csv\\salary.csv')
print(salary)
print(salary.isna().sum())
salary = salary.dropna()
print(salary.isna().sum())

print('Education levels in this population : ', salary['Education Level'].unique())
print('DIfferent jobs in this population : ', salary['Job Title'].unique())

# statistics : 
    # descriptive
gender_count = salary['Gender'].value_counts()
age_gender = salary.groupby('Gender')['Age'].agg(np.mean)
age_gender = age_gender.sort_index(axis = 0, ascending = False)
print('Number of Male and Female.')
print(gender_count)
print('Average Male and Female age.')
print(age_gender)

Avg_salary = salary.groupby(['Education Level', 'Gender'])['Salary'].agg(np.mean)
print('Average salary difference between gender and education levels.')
Avg_salary = Avg_salary.reset_index()
print(Avg_salary)

Avg_salary_pivot = pd.pivot_table(data = salary, values = 'Salary', index = 'Education Level', columns = 'Gender', aggfunc = [np.mean])
Avg_salary_pivot = Avg_salary_pivot.sort_index(axis = 1, ascending = False)
print(Avg_salary_pivot)

# null hypothesis : 
        # There is no significant salary difference between education level. : kruskal wallis h test 
stat_kwh, pvalue_education = stat.kruskal(salary[salary['Education Level'] == "Bachelor's"]['Salary'], salary[salary['Education Level'] == "Master's"]['Salary'], salary[salary['Education Level'] == "PhD"]['Salary'])
print('There is significant difference of salary between Education levels.')
print('P-value', round(pvalue_education, 2))
        # There is no significant salary difference between gender. : wilcoxon rank sum test
stat_wrs, pvalue_gender = stat.ranksums(salary[salary['Gender'] == 'Male']['Salary'], salary[salary['Gender'] == 'Female']['Salary'])
print('There is no significant difference of salary between Gender.')
print('P-value', round(pvalue_gender, 2))

# correlation study : Years of experience and salary
corr, pvalue_exp = stat.spearmanr(salary['Years of Experience'], salary['Salary'])
print('There is significant correlation between Years of Experience and Salary.')
print('Correlation coefficient :', corr)
print('P-value :', round(pvalue_exp, 2))

# data visualization
sns.set_style('whitegrid')

sns.histplot(x = 'Age', data = salary, color = 'lightpink')
plt.axvline(salary['Age'].mean(), linestyle = 'dashed', color = 'navy', label = 'Average employee age')
plt.xlabel('Age')
plt.title('Employee age')
plt.legend()
plt.show()

sns.histplot(x = 'Salary', hue = 'Education Level', data = salary, multiple = 'stack', alpha = 0.6, palette = sns.cubehelix_palette(3, dark = .30, light = .70, reverse = False))
plt.xlabel('salary')
plt.title('Education level salary')
plt.show()

sns.catplot(x = 'Education Level', y = 'Salary', data = salary, kind = 'box', hue = 'Gender', whis = [0, 100], palette = sns.cubehelix_palette(3, dark = .30, light = .70, reverse = True))
plt.title('Average Salary comparison between education levels and gender.')
plt.xlabel('Education levels')
plt.ylabel('Salary')
plt.show()

sns.relplot(x = 'Years of Experience', y = 'Salary', data = salary, kind = 'scatter', hue = 'Education Level', palette = sns.cubehelix_palette(3, dark = .25, light = .75))
plt.title('Relationships between Years of Experience and Salary.')
plt.show()

sns.relplot(x = 'Age', y = 'Years of Experience', data = salary, kind = 'scatter', hue = 'Education Level', palette = sns.cubehelix_palette(3, dark = .25, light = .75))
plt.title('Relationships between Age and Years of Experience.')
plt.show()

sns.catplot(y = 'Years of Experience', data = salary, kind = 'count', palette = sns.cubehelix_palette(len(salary['Years of Experience'].unique()), dark = .25, light = .75))
plt.title('Years of experience.')
plt.show()

sns.catplot(x = 'Education Level', y = 'Salary', hue = 'Gender', data = Avg_salary, kind = 'bar', palette = sns.cubehelix_palette(3, dark = .25, light = .75))
plt.title('Average Salary comparison between Education Levels and Gender.')
plt.show()


# predict salary by linear regression
# เปลี่ยน categorical variables ให้เป็นตัวเลขให้หมด
lbl = LabelEncoder()
salary['Gender'] = lbl.fit_transform(salary['Gender'])
salary['Education Level'] = lbl.fit_transform(salary['Education Level'])
salary['Job Title'] = lbl.fit_transform(salary['Job Title'])
print(salary)

# show model and coefficient, pvalue by statsmodels
X = salary.drop('Salary', axis = 1)
Y = salary['Salary']

X = sm.add_constant(X)
model = sm.OLS(Y, X)
result = model.fit()
result = result.summary2()
print(result)

# scikitlearn for prediction salary
X = salary.drop('Salary', axis = 1)
Y = salary['Salary']
X_train, X_test, Y_train, Y_test = train_test_split(X.values, Y.values, test_size = 0.2, random_state = 123)
model = LinearRegression()
model.fit(X_train, Y_train)

Y_predict_test = model.predict(X_test) 
mse = mean_squared_error(Y_test, Y_predict_test)
print('If employee profile is composed of ', X_test, ', respectively.')
print('Salary of that employee will be ', Y_predict_test)
print('Mean squared error = ', mse)

input = np.array([[60, 1, 2, 1, 30]])
Y_predict_real = model.predict(input)
print('If employee profile is composed of ', input, ', respectively.')
print('Age : 60, Gender : Male, Education Level : PhD, Job : Data analyst, Years of experience : 30')
print('Salary of that employee will be ', Y_predict_real)

