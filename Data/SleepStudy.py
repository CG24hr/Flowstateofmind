import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
import statsmodels.api as sm
import math

class observational() : 
    def cohort(self, array) : 
        self.Risk_Exposed = array[0, 0] / (array[0, 0] + array[0, 1])
        self.Risk_NonExposed = array[1, 0] / (array[1, 0] + array[1, 1])
        self.RR = self.Risk_Exposed / self.Risk_NonExposed
        self.CI_low, self.CI_high = stats.norm.interval(0.95, math.sqrt((1/array[0, 0]) + (1/array[0, 1]) + (1/array[1, 0]) + (1/array[1, 1])))
        self.chi, self.pvalue, self.dof, self.expected = stats.chi2_contingency(array)
        return self.RR, self.CI_low, self.CI_high, self.pvalue
    def logisticRegression (self, x, y) :
        X = sm.add_constant(x)
        model = sm.Logit(y, X)
        result = model.fit()
        result = result.summary2()
        return result.tables[1]

    

sleep = pd.read_csv('D:\\Users\\Desktop\\Python code\\GitHub\\Flowstateofmind\\Data\\csv\\Sleep_Efficiency.csv')
sleep = sleep.dropna()
sleep['Bedtime'] = pd.to_datetime(sleep['Bedtime'], utc = True)
sleep['Wakeup time'] = pd.to_datetime(sleep['Wakeup time'], utc = True)

print(sleep.columns)
print(sleep)

# descriptive study 
gender = sleep['Gender'].value_counts()
gender_duration = sleep.groupby('Gender')['Sleep duration'].mean()
gender_smoking = sleep.groupby('Gender')['Smoking status'].value_counts()
print('Number of each gender in this study.')
print(gender)
print('Average sleep duration between Male and female in this study.')
print(gender_duration)
print('Comparison between number of Smoker and non-Smoker between Male and Female in this study.')
print(gender_smoking)

print('Average Sleep efficiency between Smoker and Alcohol drinker.')
substance_efficiency = pd.pivot_table(values = 'Sleep efficiency', index = 'Smoking status', columns = 'Alcohol consumption', data = sleep, aggfunc = np.mean)
print(substance_efficiency)



# visualization
sns.set_style('whitegrid')
sns.set_palette('flare')
sns.histplot(x = 'Age', data = sleep, hue = 'Gender', alpha = 0.5, multiple = 'stack')
plt.title('Age in each group')
plt.xlabel('Age')

g = sns.catplot(x = 'Exercise frequency', y = 'Deep sleep percentage', data = sleep, kind = 'box', whis = [0, 100], sym = '')
g.fig.suptitle('Exercise frequency and quality of sleep')
g.set(xlabel = 'Exercise frequency', ylabel = 'Deep sleep percentage')
plt.show()

sns.countplot(x = 'Smoking status', data = sleep, hue = 'Gender')
plt.title('Number of smoker in each Gender')

g = sns.relplot(x = 'Deep sleep percentage', y = 'Sleep efficiency', kind = 'scatter', data = sleep, hue = 'Age', s = sleep['Sleep duration']*5)
g.fig.suptitle('Relationships between Deep sleep percentage and Sleep efficiency.')
g.set(xlabel = 'Deep sleep percentage', ylabel = 'Sleep efficiency')

g = sns.catplot(x = 'Smoking status', y = 'Sleep efficiency', data = sleep, kind = 'bar', hue = 'Alcohol consumption', ci = False)
g.fig.suptitle('Sleep efficiency comparison between Smoker and Non-smoker, Alcohol drinker.')
g.set(xlabel = 'Smoking status', ylabel = 'Sleep efficiency')
plt.show()

# Correlation between snoring_rate and OxygenSat in all stress level
corr, pvalue = stats.spearmanr(sleep['Deep sleep percentage'], sleep['Sleep efficiency'])
print('Correlation coefficient between Deep sleep percentage and Sleep efficiency :', round(corr, 2))
print('p-value :', round(pvalue, 2))


# cohort : Smoker vs. non-Smoker group and Sleep efficiency : sleep efficiency < 85 indicated poor
    # Null hypothesis : Smoking does not relate with increasing risk of poor sleep efficiency
sleep_efficiency_categories = []
for index, rows in sleep.iterrows() : 
    if rows['Sleep efficiency'] < 0.85 : 
        sleep_efficiency_categories.append('Poor')
    else : 
        sleep_efficiency_categories.append('Good')
sleep_efficiency_categories = np.array(sleep_efficiency_categories)       
sleep['Sleep efficiency quality'] = sleep_efficiency_categories

cohort = pd.crosstab(sleep['Smoking status'], sleep['Sleep efficiency quality'])
cohort = cohort.sort_index(axis = 0, ascending = False)
cohort = cohort.sort_index(axis = 1, ascending = False)
print(cohort)
cohort_array = cohort.values
print(cohort_array)

study = observational()
RR, CIlow, CIhigh, pvalue_smoking = study.cohort(cohort_array)
print('Smoking does not significantly increase risk of poor sleep efficiency.')
print('Relative risk :', round(RR, 2))
print('95%CI', [round(CIlow, 2), round(CIhigh, 2)])
print('P-value :', round(pvalue_smoking, 2))


# Multiple logistic regression between effect of Smoking, Alcohol consumption, Caffeine consumption, REM sleep percentage and Sleep efficiency
map_dict = {'Yes':1, 'No':0, 'Poor':1, 'Good':0}
sleep['Smoking status'] = sleep['Smoking status'].map(map_dict)
sleep['Sleep efficiency quality'] = sleep['Sleep efficiency quality'].map(map_dict)

x = sleep[['Smoking status', 'Alcohol consumption', 'Caffeine consumption', 'REM sleep percentage']]
y = sleep['Sleep efficiency quality']

summary = study.logisticRegression(x, y)
print(summary)

print('Alcohol consumption significantly increase risk of poor sleep efficiency.')
print('Odd ratio :', round(np.exp(summary.iloc[2, 0]), 2))
print('95% CI', [round(np.exp(summary.iloc[2, -2]), 2), round(np.exp(summary.iloc[2, -1]), 2)])