import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import numpy as np 
df = pd.read_csv('D:\\Users\\Desktop\\Datacamp\\CTS data.csv')
print(df)

# correlation between SNCV and FR 
cts = df[df['CTS'] == 1]
print(cts)

age_mean = cts.pivot_table(values = 'age', index = 'sex', columns= 'side', aggfunc = np.mean, margins = False)
print(age_mean)

side = cts.groupby('sex')['side'].value_counts()
print(side)

cts['SNCV'].hist(bins = 10, alpha = 0.75)
plt.title('SNCV')
plt.show()
cts['FR'].hist(bins = 6, alpha = 0.75)
plt.title('FR')
plt.show()


print('correlation coefficient between SNCV and FR in CTS patients : ', cts['SNCV'].corr(cts['FR'])) # .corr จะเป็นวิธี pearson's correlation
sns.lmplot(x = 'SNCV', y = 'FR', data = cts, ci = 95) 
plt.show()

# แต่จริงๆควรต้องทดสอบ normal distribution ก่อน ถ้า non normally distributed ก็ใช้ spearman's correlation
corr, pvalue = stats.spearmanr(cts['SNCV'], cts['FR'])
print(corr)
print(pvalue)