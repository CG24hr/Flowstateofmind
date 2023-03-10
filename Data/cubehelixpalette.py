import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stat
import statsmodels.api as sm

# descriptive study
# visualization
# statistics
       # multiple linear regression : ladder score ( happiness score )

happiness = pd.read_csv('D:\\Users\\Desktop\\Python code\\GitHub\\Flowstateofmind\\Data\\csv\\worldhappiness2021.csv')
print(happiness.columns)
happiness = happiness.loc[:, ['Country name', 'Regional indicator', 'Ladder score',
       'Standard error of ladder score', 'upperwhisker', 'lowerwhisker',
       'Logged GDP per capita', 'Social support', 'Healthy life expectancy',
       'Freedom to make life choices', 'Generosity',
       'Perceptions of corruption', 'Dystopia + residual']]
happiness = happiness.dropna()
print(happiness)

# description

most_happiness = happiness.sort_values('Ladder score', ascending = False)
most_happiness = most_happiness.head(10)
print(most_happiness)

most_corruption = happiness.sort_values('Perceptions of corruption', ascending = False)
most_corruption = most_corruption.head(10)
print(most_corruption)

regional = happiness['Regional indicator']
print(regional.unique())

regional_happiness = happiness.groupby('Regional indicator')['Ladder score'].agg(np.mean)
regional_happiness = regional_happiness.sort_values(ascending = False)
regional_happiness = regional_happiness.reset_index()
print(regional_happiness)

# visualization

sns.set_style('whitegrid')
my_palette = sns.cubehelix_palette(10, dark=.25, light=.75)
my_palette2 = sns.cubehelix_palette(2, dark=.4, light=.6)


g = sns.catplot(x = 'Ladder score', y = 'Country name', data = most_happiness, kind = 'bar', palette = my_palette)
g.set(xlabel = 'happiness score', ylabel = 'Countries')
g.fig.suptitle('Most happy countries')

g = sns.catplot(x = 'Ladder score', y = 'Regional indicator', data = regional_happiness, kind = 'bar', palette = my_palette)
g.set(xlabel = 'happiness score', ylabel = 'Regional')
g.fig.suptitle('Most happiness regional')


g = sns.catplot(x = 'Country name', y = 'Perceptions of corruption', data = most_corruption, kind = 'bar', palette = my_palette)
g.set(xlabel = 'Countries', ylabel = 'Corruption rates')
g.fig.suptitle('Most corruption countries')
plt.xticks(rotation = 90)

happiness_WEU_SEA = happiness[(happiness['Regional indicator'] == 'Western Europe') | (happiness['Regional indicator'] == 'Southeast Asia')]
g = sns.catplot(x = 'Regional indicator', y = 'Ladder score', data = happiness_WEU_SEA, kind = 'box', sym = '', whis = [0, 100],  palette = my_palette2)
g.set(xlabel = 'Countries', ylabel = 'Happiness score')
g.fig.suptitle('Regional happiness')
plt.show()

sns.lmplot(x = 'Healthy life expectancy', y = 'Ladder score', data = happiness, ci = 95)
sns.set_palette("colorblind")
plt.title('Happiness score and Healthy life expectancy')
plt.show()

g = sns.relplot(x = 'Freedom to make life choices', y = 'Ladder score', data = happiness, kind = 'scatter', hue = 'Regional indicator', s = happiness['Standard error of ladder score']*500, alpha = 0.8, palette = my_palette)
g.set(xlabel = 'Freedom', ylabel = 'Happiness score')
plt.title('Happiness score and Freedom to make life choices')
g = sns.relplot(x = 'Perceptions of corruption', y = 'Ladder score', data = happiness, kind = 'scatter', hue = 'Regional indicator', s = happiness['Standard error of ladder score']*500, alpha = 0.8, palette = my_palette)
g.set(xlabel = 'Corruption rates', ylabel = 'Happiness score')
plt.title('Happiness score and Perceptions of corruption')
plt.show()

sns.histplot(x='Ladder score', data=happiness)
plt.axvline(x = happiness['Ladder score'].mean(), color = 'darkgrey', linestyle = 'dashed', label = 'Average World happiness score')
plt.legend()
plt.title('World happiness score')
plt.show()


# statistics
# correlation study
corr, pvalue = stat.spearmanr(happiness['Healthy life expectancy'], happiness['Ladder score'])
print(corr)
print(pvalue)

# multiple linear regression
X = happiness[['Healthy life expectancy', 'Freedom to make life choices', 'Perceptions of corruption']]
Y = happiness['Ladder score']

X = sm.add_constant(X)
model = sm.OLS(Y ,X)
result = model.fit()
result = result.summary2()
print(result)

# compare between region
# Mannwhitney : ladder score between Western europe and southeast asia
stats, pvalue = stat.mannwhitneyu(happiness[happiness['Regional indicator'] == 'Western Europe']['Ladder score'], happiness[happiness['Regional indicator'] == 'Southeast Asia']['Ladder score'])
print(stats)
print(pvalue)