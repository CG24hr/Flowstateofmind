# customize dataframe with columns of inclusion and exclusion criteria
# randomization allocation into experimental & control group ( by .sample() )
# plot distribution with histogram

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

class RCT :
    def distribution(self, data) : 
        self.stat_shapiro, self.pvalue_shapiro = stats.shapiro(data)
        return self.pvalue_shapiro 

    def intradiff(self, data1, data2) : 
        self.intradiff = data2 - data1
        self.stat_shapiro, self.pvalue_shapiro = stats.shapiro(self.intradiff)
        if self.pvalue_shapiro >= 0.05 :
            self.stat, self.pvalue = stats.ttest_rel(data1, data2)
        else :
            self.stat, self.pvalue = stats.wilcoxon(data1, data2)
        return self.pvalue
    
    def interdiff(self, data1, data2) : 
        self.stat_shapiro_1, self.pvalue_shapiro_1 = stats.shapiro(data1)
        self.stat_shapiro_2, self.pvalue_shapiro_2 = stats.shapiro(data2)
        if self.pvalue_shapiro_1 >= 0.05 and self.pvalue_shapiro_2 >= 0.05 :
            self.stat, self.pvalue = stats.ttest_ind(data1, data2)
        else :
            self.stat, self.pvalue = stats.mannwhitneyu(data1, data2)
        return self.pvalue


# create population before including or excluding / randomization
n = int(input('Enter number of sample size : '))
ID = []
for i in range(n) : 
    ID.append(i+1)
ID = np.array(ID)


age = np.round(np.random.normal(60, 10, n), 0)

type = np.random.choice(['extracapsular', 'intracapsular'], n)
surgery = np.random.choice(['DHS', 'External fixator', 'Gamma nail'], n)
underlying = np.random.choice(['cardiovascular', 'neurological', 'systemic disease', 'none'], n)

data = {'ID':ID, 'age':age, 'fracture' : type, 'surgery':surgery, 'underlying':underlying}
df = pd.DataFrame(data)
df = df.set_index('ID')
print(df)

eligible = df.query('age >= 50 and fracture == "intracapsular" and surgery == "Gamma nail" and underlying == "none"')
print(eligible)

eligible['group'] = np.random.choice(['control', 'experimental'], p = [0.5, 0.5], size = len(eligible.index))
print(eligible)

eligible[eligible['group'] == 'control']['age'].hist(bins = 10, alpha = 0.5)
eligible[eligible['group'] == 'experimental']['age'].hist(bins = 10, alpha = 0.5)
plt.title('Age distribution in control and experimental group')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

print('descriptive statistics of age between two comparison groups')
print(eligible.groupby('group')['age'].describe())

plt.boxplot([eligible[eligible['group'] == 'control']['age'], eligible[eligible['group'] == 'experimental']['age']], positions = [1, 2])
plt.xticks([1, 2], ['control', 'experimental'])
plt.title('Interquantile range of age')
plt.show()


control = eligible[eligible['group'] == 'control']
experimental = eligible[eligible['group'] == 'experimental']
print(control)
print(experimental)

# test for normality and compare baseline characteristic between control & experimental groups
stat_exp, pvalue_exp = stats.shapiro(experimental['age'])
stat_con, pvalue_con = stats.shapiro(control['age'])
if pvalue_exp and pvalue_con >= 0.05 :
    stat_age, pvalue_age = stats.ttest_ind(control['age'], experimental['age'])
    print('The difference between age of two group were examined by independent t-test.')
    print('The significant value of difference between control and experimental age : {}'.format(pvalue_age))
else : 
    stat_age, pvalue_age = stats.mannwhitneyu(control['age'], experimental['age'])
    print('The difference between age of two group were examined by Mann-whitney U test.')
    print('The significant value of difference between control and experimental age : {}'.format(pvalue_age))


# input numeric rating score of pain intensity at walk 
day1_pain_con = np.round(stats.norm.rvs(6, 1, len(control.index)), 0)
day1_pain_exp = np.round(stats.norm.rvs(6, 1, len(experimental.index)), 0)

day5_pain_con = np.round(stats.norm.rvs(4, 1, len(control.index)), 0)
day5_pain_exp = np.round(stats.norm.rvs(2, 1, len(experimental.index)), 0)

control['day1_pain'] = day1_pain_con
control['day5_pain'] = day5_pain_con
experimental['day1_pain'] = day1_pain_exp
experimental['day5_pain'] = day5_pain_exp

diff_pain_con = control['day1_pain'] - control['day5_pain'] 
diff_pain_exp = experimental['day1_pain'] - experimental['day5_pain'] 
control['difference'] = diff_pain_con
experimental['difference'] = diff_pain_exp

print(control)
print(experimental)

# plot
control['difference'].hist(bins = [1,2,3,4,5,6,7,8,9,10], alpha = 0.75, label = 'Control group')
experimental['difference'].hist(bins = [1,2,3,4,5,6,7,8,9,10], alpha = 0.75, label = 'Experimental group')
mean_diff_con = control['difference'].mean()
mean_diff_exp = experimental['difference'].mean()
plt.title('Distribution of pain intensity difference during walk in both groups.')
plt.xlabel('Pain intensity (Numeric rating scale)')
plt.axvline(mean_diff_con, color = 'navy', linestyle = 'dashed', linewidth = 1, label = 'mean difference of control group')
plt.axvline(mean_diff_exp, color = 'red', linestyle = 'dashed', linewidth = 1, label = 'mean difference of experimental group')
plt.legend()
plt.show()

# เนื่องจาก เป็นการวัด mean difference ระหว่าง 2 กลุ่ม ถึงจะเป็น categorical variable ก็ควรใช้ ttest จึงเหมาะสมกว่า chi square ซึ่งใช้วัด frequency
# test for normality of dependent variables


# pre-post difference in control group
study1 = RCT()
pvalue_con_dis =  study1.distribution(control['difference'])
if pvalue_con_dis >= 0.05 : 
    print('The difference of pain intensity between pre-post intervention of control group is normally distributed.')
else :
    print('The difference of pain intensity between pre-post intervention of control group is not normally distributed.')
print('p-value = ', pvalue_con_dis)

pvalue_con_diff = study1.intradiff(control['day1_pain'], control['day5_pain'])
if pvalue_con_diff >= 0.05 : 
    print('There is no significant difference of pain intensity between pre and post intervention in control group.')
else : 
    print('There is significant difference of pain intensity between pre and post intervention in control group.')
print('p-value = ', pvalue_con_diff)

# pre-post difference in experimental 
study2 = RCT()
pvalue_exp_dis =  study2.distribution(experimental['difference'])
if pvalue_exp_dis >= 0.05 : 
    print('The difference of pain intensity between pre-post intervention of experimental group is normally distributed.')
else :
    print('The difference of pain intensity between pre-post intervention of experimental group is not normally distributed.')
print('p-value = ', pvalue_exp_dis)

pvalue_exp_diff = study2.intradiff(experimental['day1_pain'], experimental['day5_pain'])
if pvalue_exp_diff >= 0.05 : 
    print('There is no significant difference of pain intensity between pre and post intervention in experimental group.')
else : 
    print('There is significant difference of pain intensity between pre and post intervention in experimental group.')
print('p-value = ', pvalue_exp_diff)

# compare difference between two independent groups
study_main = RCT()
pvalue_main = study_main.interdiff(control['difference'], experimental['difference'])
if pvalue_main >= 0.05 : 
    print('There is no significant difference of pain intensity between control and experimental group after intervention.')
else : 
    print('There is significant difference of pain intensity between control and experimental group after intervention.')
print('p-value = ', pvalue_main)

