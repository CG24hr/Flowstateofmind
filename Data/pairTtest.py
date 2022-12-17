# use np.random.normal(mean, S.D., size = n) to create boths pre-test and post-test
# import pandas to create dataframe 
# display histogram of post-test data distribution 
# write objected oriented programming 
# method 1.) distribution() 2.) pairedTtest()
# test normal distribution of post-test data by shapiro-wilk
    # null hypothesis : the data has normal distribution -> p-value > 0.05
    # if p-value > 0.05 :
        # hypothesis testing by paired t-test 

class pairedTtest :
    def __init__(self,pretest, posttest) : 
        import scipy.stats 
        self.pretest = pretest
        self.posttest = posttest
        self.SciPy = scipy.stats

    def distribution(self) :
        self.statistic, self.pvalue = self.SciPy.shapiro(self.posttest)
        print('Shapiro-Wilk : test statistic = {}, p-value = {}'.format(self.statistic, self.pvalue))

    def hypothesis(self) : 
        # Perform paired t-test
        if self.pvalue > 0.05 :
            t_statistic, t_pvalue = self.SciPy.ttest_rel(self.pretest, self.posttest)
            # Print results
            print('student paired t-test : test statistic = {}, p-value = {}'.format(t_statistic, t_pvalue))
        else : 
            print('The assumption test was failed. Please use others statistical method.')

# compare SBP before and after cardiopulmonary exercise in same persons.
n = int(input('sample size : '))
ID = []
for i in range(1,n+1) :
    ID.append(i)
import numpy as np 
preSBP = np.random.normal(150, 5, size = n)
postSBP = np.random.normal(130, 5, size = n)
ID_np = np.array(ID)

SBP = {}
SBP['participants ID'] = ID
SBP['pre-exercise SBP'] = preSBP
SBP['post-exercise SBP'] = postSBP 

import pandas as pd 
df = pd.DataFrame(SBP)
df = df.set_index('participants ID')
dfPre = df.loc[:,['pre-exercise SBP']]
dfPost = df.loc[:,['post-exercise SBP']]
print(df)
print(dfPre.describe())
print(dfPost.describe())

import matplotlib.pyplot as plt
plt.hist(dfPost,bins = 5)
plt.xlabel('Systolic BP')
plt.ylabel('Number of participants')
plt.show()

# call class & function 
research = pairedTtest(dfPre, dfPost)
research.distribution()
research.hypothesis()