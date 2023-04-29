import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import scipy.stats as stats
import pingouin as pg
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Explore data 
emission = pd.read_csv('D:\\Users\\Desktop\\Python code\\GitHub\\Flowstateofmind\\Data\\csv\\emissionFAOSTAT.csv')
print(emission)
print(emission.columns)
print(emission.info())
print(emission.isna().sum())
emission = emission[['Area', 'Element', 'Item', 'Year', 'Unit', 'Value']]
print(emission)

topsix_gdp = pd.read_csv('D:\\Users\\Desktop\\Python code\\GitHub\\Flowstateofmind\\Data\\csv\\top_six_economies.csv')
usa_gdp = topsix_gdp[(topsix_gdp['Country Name'] == 'United States') & (topsix_gdp['Year'] >= 2001) & (topsix_gdp['Year'] <= 2020)]
usa_gdp_percap = usa_gdp[['Year', 'GDP per capita (current US$)']]
print(usa_gdp_percap)
china_gdp = topsix_gdp[(topsix_gdp['Country Name'] == 'China') & (topsix_gdp['Year'] >= 2001) & (topsix_gdp['Year'] <= 2020)]
china_gdp_percap = usa_gdp[['Year', 'GDP per capita (current US$)']]
china_gdp_percap = usa_gdp[['Year', 'GDP per capita (current US$)']]
print(china_gdp_percap)


# Objective of study : Greenhouse gas comparison ['CO2', 'CH4', 'N2O'] between each area
emission['Element'] = emission['Element'].str.replace('Emissions ', '')
emission['Element'] = emission['Element'].str.replace('(', '')
emission['Element'] = emission['Element'].str.replace(')', '')
print('Countries in this study : ', emission['Area'].unique())
print('Green house gas in this study : ', emission['Element'].unique())


# Descriptive study
    # Carbondioxide emissions in Thailand over the last two decades.
thai = emission[emission['Area'] == 'Thailand']
thai_carbon = thai[thai['Element'] == 'CO2']
thai_carbon_emission = thai_carbon.groupby('Item')['Value'].mean()
thai_carbon_emission = thai_carbon_emission.reset_index()
print('Average Carbondioxide emissions in Thailand over the last two decades.')
print(thai_carbon_emission)

thai_carbon_sum = pd.pivot_table(data = thai_carbon, values = 'Value', index = 'Year', columns = 'Element', aggfunc = np.sum)
print(thai_carbon_sum)
    # Methane and Nitrous oxides in Thaialnd over the last two decades.
thai_methane_nitrous = thai[thai['Element'].isin(['CH4', 'N2O'])]
thai_methane_nitrous = thai_methane_nitrous.groupby(['Element', 'Item'])['Value'].mean()
thai_methane_nitrous = thai_methane_nitrous.reset_index()
print('Average Methane and Nitrous Oxide in Thailand over the last two decades.')
print(thai_methane_nitrous)

    # Compare total CO2 emission between USA and China over the last two decades
usa_china = emission[emission['Area'].isin(['United States of America', 'China, mainland'])]
usa_china_carbon = usa_china[usa_china['Element'] == 'CO2']
usa_china_carbon_total = usa_china_carbon.groupby('Area')['Value'].mean()
print('Average CO2 emission between USA and China over the last two decades.')
print(usa_china_carbon_total)

usa_china_carbon_year = usa_china_carbon.groupby(['Area', 'Year'])['Value'].sum()
usa_china_carbon_year = usa_china_carbon_year.reset_index()
print(usa_china_carbon_year)

usa_carbon_year = usa_china_carbon_year[usa_china_carbon_year['Area'] == 'United States of America']
gdp_carbon_usa = usa_carbon_year.merge(usa_gdp_percap, on = 'Year', how = 'inner')
print(gdp_carbon_usa)
china_carbon_year = usa_china_carbon_year[usa_china_carbon_year['Area'] == 'China, mainland']
gdp_carbon_china = china_carbon_year.merge(china_gdp_percap, on = 'Year', how = 'inner')
print(gdp_carbon_china)
gdp_usa_china_carbon = pd.concat([gdp_carbon_usa, gdp_carbon_china], ignore_index = False)
print(gdp_usa_china_carbon)

# Hypothesis testing : 
    # Thailand had been emitted Greenhouse gas over 2011-2020 more than 2001-2010 significantly.
ten_th = thai_carbon[(thai_carbon['Year'] >= 2001) & (thai_carbon['Year'] < 2011)]
twenty_th = thai_carbon[(thai_carbon['Year'] >= 2011) & (thai_carbon['Year'] < 2021)]
ten_th = pd.pivot_table(data = ten_th, index = 'Year', values = 'Value', aggfunc = np.sum)
twenty_th = pd.pivot_table(data = twenty_th, index = 'Year', values = 'Value', aggfunc = np.sum)
two_decades_th = pd.concat([ten_th, twenty_th], ignore_index = False)
print(two_decades_th)
stat, pvalue_th_carbon = stats.wilcoxon(two_decades_th.iloc[0:10, 0], two_decades_th.iloc[10:20, 0])
print('There is significant of increasing CO2 emission in Thailand between the last two decades.')
print('P-value :', pvalue_th_carbon)
    # USA had been emitted Greenhouse gas more than China over the last two decades significantly. 
stat, pvalue_usa_china_carbon = stats.mannwhitneyu(usa_china_carbon_year[usa_china_carbon_year['Area'] == 'China, mainland']['Value'], usa_china_carbon_year[usa_china_carbon_year['Area'] == 'United States of America']['Value'])
print('There is significantly different CO2 emission between USA and China over the last two decades.')
print('P-value :', pvalue_usa_china_carbon)
    # CO2 emission has positive correlation with GDP per Capita growth
        # USA
corr, pvalue_emis_carbon_usa_corr = stats.spearmanr(gdp_carbon_usa['GDP per capita (current US$)'], gdp_carbon_usa['Value'])
print('There is no significant correlation between GDP growth and CO2 emission in USA over the last two decades. p-value : ', pvalue_emis_carbon_usa_corr)
        # China
corr, pvalue_emis_carbon_china_corr = stats.spearmanr(gdp_carbon_china['GDP per capita (current US$)'], gdp_carbon_china['Value'])
print('There is  significantly positive correlation between GDP growth and CO2 emission in China over the last two decades. p-value : ', pvalue_emis_carbon_china_corr)

# Data visualization
sns.set_style('whitegrid')
sns.barplot(data = thai, x = 'Item', y = 'Value', hue = 'Element', palette = sns.color_palette('Reds', 2)[::-1])
plt.xlabel('Causes')
plt.ylabel('Unit(Kilotonnes)')
plt.title('Average Carbondioxide emissions in Thailand over the last two decades.')
plt.show()

sns.barplot(data = thai_methane_nitrous, x = 'Element', y = 'Value', hue = 'Item', palette = sns.color_palette('Reds', 5)[::-1]),
plt.xlabel('Causes')
plt.ylabel('Unit(Kilotonnes)')
plt.title('Average Methane and Nitrous Oxide in Thailand over the last two decades.')
plt.show()

sns.catplot(data = usa_china_carbon, x = 'Item', y = 'Value', hue = 'Area', kind = 'point', ci = False, palette = sns.color_palette('Reds', 2)[::-1])
plt.xlabel('Causes')
plt.ylabel('Unit(Kilotonnes)')
plt.title('Average CO2 emissions comparison between USA and China over the last two decades.')
plt.show()

sns.lineplot(data = thai_carbon, x = 'Year', y = 'Value', ci = False)
plt.xticks(thai_carbon['Year'].unique(), rotation = 90)
plt.xlabel('Years')
plt.ylabel('Unit(Kilotonnes)')
plt.title('CO2 emissions in Thailand over the last two decades.')
plt.show()

sns.lineplot(data = usa_china_carbon_year, x = 'Year', y = 'Value', hue = 'Area', ci = False, palette = sns.color_palette('Reds', 2)[::-1])
plt.xticks(usa_china_carbon['Year'].unique(), rotation = 90)
plt.xlabel('Years')
plt.ylabel('Unit(Kilotonnes)')
plt.title('CO2 emissions comparison between USA and China over the last two decades.')
plt.show()

sns.scatterplot(data = gdp_usa_china_carbon, x = 'GDP per capita (current US$)', y = 'Value', hue = 'Area', palette = sns.color_palette('Reds', 2)[::])
plt.title('Relationships between GDP per capita and CO2 emissions in USA and China.')
plt.xlabel('GDP per Capita')
plt.ylabel('CO2 emissions')
plt.show()


# Machine learning
    # show model by statmodels.api
X = gdp_carbon_china[['Year', 'GDP per capita (current US$)']]
Y = gdp_carbon_china['Value']
X = sm.add_constant(X)
model = sm.OLS(Y, X)
result = model.fit()
result = result.summary2()
print(result)
    # train data by sklearn
X = gdp_carbon_china[['Year', 'GDP per capita (current US$)']]
Y = gdp_carbon_china['Value']
X_train, X_test, Y_train, Y_test = train_test_split(X.values, Y.values, test_size = 0.2, random_state = 123)
model = LinearRegression()
model.fit(X_train, Y_train)
        # test data
Y_predict_test = model.predict(X_test)
MAE = mean_absolute_error(Y_test, Y_predict_test)
MSE = mean_squared_error(Y_test, Y_predict_test)
Rsquare = r2_score(Y_test, Y_predict_test)
print('Mean absolute error : ', MAE)
print('Mean squared error : ', MSE)
print('R**2_score : ', Rsquare)
        # predict Y from new input
input = np.array([[2023, 70000]])
Y_predict_new = model.predict(input)
print('If the GDP per capita in China is 70000 USD in 2023, the total CO2 emission would be {}'.format(Y_predict_new))
            # visualize model
fig, (ax0, ax1) = plt.subplots(1, 2, sharey = True)
sns.residplot(data = gdp_carbon_china, x = 'GDP per capita (current US$)', y = 'Value', ax = ax0)
plt.title('Linear regression model')
sns.residplot(data = gdp_carbon_china, x = 'Year', y = 'Value', ax = ax1)
plt.title('Linear regression model')
plt.show()
