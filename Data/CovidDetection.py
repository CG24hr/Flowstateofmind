import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
covid = pd.read_csv('D:\\Users\\Desktop\\Python code\\GitHub\\Flowstateofmind\\Data\\csv\\detect-covid-data.csv')
print(covid)
print(covid.columns)


covid = covid.iloc[:, [1,2,3,5,8,11,14,17,19,38]]
covid = covid.set_index(['continent', 'location']).sort_index()
covid_2022 = covid[covid['date'] >= '2022-01-01']

covid_2022['total_cases'] = covid_2022.groupby('location')['new_cases'].cumsum()
covid_2022['total_deaths'] = covid_2022.groupby('location')['new_deaths'].cumsum()
covid_2022['total_vaccinations'] = covid_2022.groupby('location')['new_vaccinations'].cumsum()
print(covid_2022)

covid_2022_th = covid_2022.loc[('Asia', 'Thailand')]
covid_2022_th = covid_2022_th[(covid_2022_th['new_cases'] > 0) & (covid_2022_th['new_vaccinations'] > 0)]
covid_2022_th['icu_patients'] = covid_2022_th['icu_patients'].fillna(0) #.fillna ใช้ replace NaN value 
covid_2022_th['hosp_patients'] = covid_2022_th['hosp_patients'].fillna(0)
print(covid_2022_th)

covid_2022_th['date'] = pd.to_datetime(covid_2022_th['date']) 
covid_2022_th['month'] = covid_2022_th['date'].dt.month
print(covid_2022_th)

plt.plot(covid_2022_th['date'], covid_2022_th['total_vaccinations'])
plt.plot(covid_2022_th['date'], covid_2022_th['total_deaths'])
plt.xlabel('2022')
plt.ylabel('Covid-19 Vaccinations')
plt.show()