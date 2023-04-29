import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import statsmodels.api as sm
import pingouin as pg
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# clean & explore data
usa_covid = pd.read_csv('D:\\Users\\Desktop\\Python code\\GitHub\\Flowstateofmind\\Data\\csv\\Covid-19USAdeath.csv')
print(usa_covid)
print(usa_covid.info())
print(usa_covid.isna().sum())
usa_covid = usa_covid[['date', 'cases', 'deaths']]
usa_covid['date'] = pd.to_datetime(usa_covid['date'])
usa_covid = usa_covid.sort_values('date', ascending = True)
print(usa_covid)
usa_covid = usa_covid.groupby('date')[['cases', 'deaths']].agg(np.sum)
usa_covid = usa_covid.reset_index()
print('Total Covid-19 Infection in USA')
print(usa_covid)  


# hypothesis 
sns.set_style('whitegrid')
    # total covid-19 cases in USA didn't linear correlation with total deaths.
        # data visualize
sns.lineplot(data = usa_covid, x = 'date', y = 'cases', label = 'Total Cases')
sns.lineplot(data = usa_covid, x = 'date', y = 'deaths', label = 'Total Deaths', color = 'red')
plt.title('Total Covid-19 cases and deaths in USA, since Jan 2020 - May 2022')
plt.xlabel('Date')
plt.ylabel('Count')
plt.show()

sns.regplot(data = usa_covid, x = 'cases', y = 'deaths', order = 2, x_bins = 10)
plt.xlabel('Total Cases')
plt.ylabel('Total Deaths')
plt.title('Relationships between Total Covid-19 cases and deaths')
plt.show()
        # statistics
corr, pvalue = stats.spearmanr(usa_covid['cases'], usa_covid['deaths'])
print('Correlation coefficient between total Covid-19 cases and total deaths : ', corr)
print('P-value : ', pvalue)
