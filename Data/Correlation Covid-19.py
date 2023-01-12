# poerform relationship statistics between COVID-19 Deaths and Vaccinations
# display as scatter plot

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import scipy.stats as stats
covid = pd.read_csv('D:\\Users\\Desktop\\Python code\\GitHub\\Flowstateofmind\\Data\\csv\\detect-covid-data.csv')
print(covid)

covid = covid.fillna(0)
covid_us_th = covid[(covid['location'] == 'United States') | (covid['location'] == 'Thailand')]
print(covid.columns)
print(covid_us_th)

covid_mortal_vacc = covid_us_th.loc[:, ['location', 'date', 'population', 'gdp_per_capita', 'new_deaths', 'weekly_icu_admissions', 'new_vaccinations']]
print(covid_mortal_vacc)

covid_mortal_vacc['total_vaccinations'] = covid_mortal_vacc.groupby('location')['new_vaccinations'].cumsum()
covid_mortal_vacc = covid_mortal_vacc.set_index('location')
covid_mortal_vacc = covid_mortal_vacc[covid_mortal_vacc['date'] >= '2021-06-01']
print(covid_mortal_vacc)

covid_mortal_vacc.loc['Thailand', :].plot(x = 'date', y = ['new_deaths', 'total_vaccinations'], secondary_y = 'total_vaccinations',kind = 'line')
plt.title('Correlations between Covid-19 vaccinations and deaths in Thailand since June 2021.')
plt.xlabel('Date')
plt.ylabel('Number of people')
plt.show()

covid_mortal_th = covid_mortal_vacc.loc['Thailand']
print(covid_mortal_th)
covid_mortal_th_startvacc =  covid_mortal_th[covid_mortal_th['date'] >= '2021-06-01']
print(covid_mortal_th_startvacc)

corr, p_value = stats.spearmanr(covid_mortal_th_startvacc.loc[: , 'total_vaccinations'], covid_mortal_th_startvacc.loc[: , 'new_deaths'])
print('Correlation coefficient between Covid-19 Vaccinations and Death in Thailand : {}'.format(corr))
print('P-value : {}'.format(round(p_value, 2)))


# scatter (continuous variables)
covid_Europe = covid[covid['continent'] == 'Europe']

covid_Europe = covid_Europe.loc[:, ['location', 'date', 'population', 'gdp_per_capita', 'new_deaths_per_million', 'weekly_icu_admissions_per_million', 'new_vaccinations_smoothed_per_million']]
covid_Europe = covid_Europe.rename(columns = {'new_vaccinations_smoothed_per_million' : 'new_vaccinations_per_million'})
covid_Europe = covid_Europe[covid_Europe['date'] >= '2021-06-01']



covid_Europe['total_vaccinations_per_million'] = covid_Europe.groupby('location')['new_vaccinations_per_million'].cumsum()
covid_Europe = covid_Europe.set_index('location')


covid_Europe.plot(x = 'total_vaccinations_per_million', y = 'new_deaths_per_million', kind = 'scatter', alpha = 0.25, s = covid_Europe['population'] / 10**6, c = 'navy')
plt.title('Correlation between Covid-19 vaccination rate and deaths rate in Europe since June 2021')
plt.show()

corr, p_value = stats.spearmanr(covid_Europe.loc[:, 'total_vaccinations_per_million'], covid_Europe.loc[:, 'new_deaths_per_million'])
print('Correlation coefficient between Covid-19 Vaccinations and Death in European countries : {}'.format(corr))
print('P-value : {}'.format(round(p_value, 2)))