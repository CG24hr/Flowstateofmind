# Perform spearman's rank correlation for stock analysis : ROE PBV ratio correlation
# calculate median and IQR and show descriptive statistics
# display line plot and scatter plot
# use standard error to compute 95% confidential interval

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import scipy.stats as stats



year = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
ROE = [29.97, 34.9, 57.0, 33.3, 36.4, 56.2, 56.7, 86.3, 144.3, 174.2]
PBV = [4.90, 5.86, 5.52, 4.68, 6.67, 8.92, 11.8, 14.6, 20.7, 22.3]
EPS = [0.17, 0.20, 0.46, 0.34, 0.36, 0.60, 0.62, 1.82, 2.99, 3.22]
PER = [12.2, 17.3, 12.8, 13.5, 18.9, 16.9, 20.2, 17.1, 14.2, 11.6]
Equity = [0.49, 0.58, 1.06, 0.97, 1.03, 1.14, 1.06, 2.14, 2.05, 1.67]
factsheet = {'Fiscal years':year, 'ROE(%)':ROE, 'PBV':PBV, 'EPS':EPS, 'PER':PER, 'Equity per share':Equity}

factsheet = pd.DataFrame(factsheet)
factsheet = factsheet.set_index('Fiscal years')
print(factsheet)

descriptive = factsheet.describe()
print(descriptive)

# add median & iqr into descriptive

median = {}
for i in factsheet.columns : 
    median[i] = factsheet[i].median()
print(median)

iqr = {}
for i in factsheet.columns :
    iqr[i] = factsheet[i].quantile(0.75) - factsheet[i].quantile(0.25)
print(iqr)

median = pd.DataFrame(median, index = ['median'])
iqr = pd.DataFrame(iqr, index = ['IQR'])
median_iqr = pd.concat([median, iqr], ignore_index = False)
print(median_iqr)

descriptive = pd.concat([descriptive, median_iqr], ignore_index = False)
print(descriptive)

# visualize 
factsheet.plot(y = ['ROE(%)', 'EPS'], secondary_y = 'EPS', marker = 'o', kind = 'line')
plt.show()

factsheet.plot(x = 'ROE(%)', y = 'PBV', kind = 'scatter')
plt.show()

# calculate correlation coefficient
corr, pvalue = stats.spearmanr(factsheet['ROE(%)'], factsheet['PBV'])
print('Correlation coefficient between return on equity and price per book value of Apple Co. : {}'.format(corr))
print('Significant value : {}'.format(pvalue))