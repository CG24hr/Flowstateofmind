# calculate sample size 
# use random module to create data 
    # patients profile of control & intervention group : age, onset, type , volume of lesion
    # outcome measurement : modified ashworth scale(MAS), Brunstrom stages of motor recovery(BS)
# plot histogram to check normal distribution
# create dataframe 
# design randomized controlled trial with objected oriented togramm
# compare profile between group
    # use a shapiro-wilk test for profile of both groups : 
        #  if normally distribution (p>0.05) : Independent t test --> P-value should be > 0.05 (no significant difference of patient's profiles between groups)
        #  else : Mann whitney U test 
# control group : give conventional therapy 
    # compare : pretest vs posttest
        # use a shapiro-wilk test to test normally distributed of dependent variables
        # use paired t test to calculate significant difference between pretest & posttest
# intervention group : give robotic therapy
    # compare : pretest vs posttest
        # use a shapiro-wilk test to test normally distributed of dependent variables
        # use paired t test to calculate significant difference between pretest & posttest
# intervention vs control group 
   # use a shapiro-wilk test to test normally distributed of posttest scores of these two groups
    # if posttest scores of both groups have normal distribution (p>0.05) :
        # independent t test 
    # else :
        # mann whitney U test



class RCT : 

    def __init__(self) :
        from scipy.stats import shapiro, ttest_rel, ttest_ind, wilcoxon, mannwhitneyu
        self.shapiro = shapiro
        self.ttest_rel = ttest_rel
        self.ttest_ind = ttest_ind
        self.wilcoxon = wilcoxon
        self.mannwhitneyu = mannwhitneyu

    def samplesize(self, confidential_level, margin_of_error) : 
        self.z = 0.0
        self.CL = {99: 2.576, 98: 2.326, 95: 1.96, 90: 1.645}
        if confidential_level in self.CL :
            self.z = self.CL[confidential_level]
        else :
            return - 1
        self.p = 0.5
        self.e = margin_of_error
        self.samplesize = ((self.z**2) * self.p * (1-self.p)) / (self.e**2)
        return self.samplesize
    
    def distribution (self, data1, data2) : 
        self.data1 = data1
        self.data2 = data2
        self.stat, self.pvalueNorm1 = self.shapiro(self.data1)
        self.stat, self.pvalueNorm2 = self.shapiro(self.data2)

    def interdiff (self) : 
        if self.pvalueNorm1 and self.pvalueNorm2 >= 0.05 : 
            self.stat, self.pvalue = self.ttest_ind(self.data1, self.data2)
        else : 
            self.stat, self.pvalue = self.mannwhitneyu(self.data1, self.data2)
        return self.pvalue

    def intradiff (self) : 
        if self.pvalueNorm2 >= 0.05 : 
            self.stat, self.pvalue = self.ttest_rel(self.data1, self.data2)
        else :
            self.stat, self.pvalue = self.wilcoxon(self.data1, self.data2)
        return self.pvalue

research = RCT()
ss = research.samplesize(95, 0.05)
ss = round(ss)
print('Appropriated sample size is : ', ss)


import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd


# Create profile & baseline clinical score  array of both groups by np.random : Age, onset, type, volume of lesion 
ID = []
for i in range(ss): 
    ID.append(i+1)
ID_np = np.array(ID)

# Quantitative (ordinal/nominal) : random.randint, Quantitative (interval/ratio) : random.normal
age = np.round(np.random.normal(50, 2, ss)).astype(int)
onset= np.round(np.random.normal(12,2, ss)).astype(int)
vol = np.random.normal(15,2, ss)


ProfileData = {'Patients ID':ID_np , 'Age':age, 'Onset':onset, 'Vol(cm3)':vol}
dfProfile = pd.DataFrame(ProfileData)
dfProfile = dfProfile.set_index('Patients ID')

dfProfile['group'] = np.random.choice(['control', 'intervention'], size = ss, p = [0.5, 0.5])
print(dfProfile)
dfProfile_con = dfProfile[dfProfile['group'] == 'control']
dfProfile_int = dfProfile[dfProfile['group'] == 'intervention']
print('Baseline characteristics of control group : ')
print(dfProfile_con)
print(dfProfile_con.describe())
print('Baseline characteristics of intervention group : ')
print(dfProfile_int)
print(dfProfile_int.describe())




# baseline clinical score

MAS_preControl = np.random.choice([0,1,2,3,4,5], len(dfProfile_con.index), p = [0.1,0.1,0.1,0.3,0.4,0.0])
MAS_postControl = np.random.choice([0,1,2,3,4,5], len(dfProfile_con.index), p = [0.2,0.3,0.3,0.1,0.1,0.0])
MAS_preInt = np.random.choice([0,1,2,3,4,5], len(dfProfile_int.index), p = [0.1,0.1,0.1,0.3,0.4,0.0])
MAS_postInt = np.random.choice([0,1,2,3,4,5], len(dfProfile_int.index), p = [0.2,0.3,0.3,0.2,0.0,0.0])

BS_preControl = np.random.choice([1,2,3,4,5,6], len(dfProfile_con.index), p = [0.2,0.3,0.2,0.1,0.1,0.1])
BS_postControl = np.random.choice([1,2,3,4,5,6], len(dfProfile_con.index), p = [0.0,0.2,0.2,0.2,0.2,0.2])
BS_preInt = np.random.choice([1,2,3,4,5,6], len(dfProfile_int.index), p = [0.2,0.3,0.2,0.1,0.1,0.1])
BS_postInt = np.random.choice([1,2,3,4,5,6], len(dfProfile_int.index), p = [0.0,0.0,0.2,0.2,0.3,0.3])


dfProfile_con['MAS_pre'] = MAS_preControl
dfProfile_con['MAS_post'] = MAS_postControl
dfProfile_con['BS_pre'] = BS_preControl
dfProfile_con['BS_post'] = BS_postControl

dfProfile_int['MAS_pre'] = MAS_preInt
dfProfile_int['MAS_post'] = MAS_postInt
dfProfile_int['BS_pre'] = BS_preInt
dfProfile_int['BS_post'] = BS_postInt

print('Baseline Clinical data of control group : ')
print(dfProfile_con)
print('Baseline Clinical data of intervention group : ')
print(dfProfile_int)


# test difference between baseline characteristics between control and intervention group (Age, Onset, Vol(cm3)) + MAS & BS before treatment
# test for normality distribution 
study = RCT()

study.distribution(dfProfile_con['Age'], dfProfile_int['Age'])
pvalue_age = study.interdiff()
if pvalue_age >= 0.05 : 
    print('There is not significant difference between age of two comparison groups')
elif pvalue_age < 0.05 :
    print('There is significant difference between age of two comparison groups')
print('p-value = ', round(pvalue_age, 2))

study.distribution(dfProfile_con['Onset'], dfProfile_int['Onset'])
pvalue_onset = study.interdiff()
if pvalue_onset >= 0.05 : 
    print('There is not significant difference between onset of two comparison groups')
elif pvalue_onset < 0.05 :
    print('There is significant difference between onset of two comparison groups')
print('p-value = ', round(pvalue_onset, 2))

study.distribution(dfProfile_con['Vol(cm3)'], dfProfile_int['Vol(cm3)'])
pvalue_vol = study.interdiff()
if pvalue_vol >= 0.05 : 
    print('There is not significant difference between Vol(cm3) of two comparison groups')
elif pvalue_vol < 0.05 :
    print('There is significant difference between Vol(cm3) of two comparison groups')
print('p-value = ', round(pvalue_vol, 2))

study.distribution(dfProfile_con['MAS_pre'], dfProfile_int['MAS_pre'])
pvalue_MAS = study.interdiff()
if pvalue_MAS >= 0.05 : 
    print('There is not significant difference between MAS before treatment of two comparison groups')
elif pvalue_MAS < 0.05 :
    print('There is significant difference between MAS before treatment of two comparison groups')
print('p-value = ', round(pvalue_MAS, 2))

study.distribution(dfProfile_con['BS_pre'], dfProfile_int['BS_pre'])
pvalue_BS = study.interdiff()
if pvalue_BS >= 0.05 : 
    print('There is not significant difference between BS before treatment of two comparison groups')
elif pvalue_BS < 0.05 :
    print('There is significant difference between BS before treatment of two comparison groups')
print('p-value = ', round(pvalue_BS, 2))



# histogram
# normality test for dependent variables
# dependent variables = difference
diff_MAS_con = dfProfile_con['MAS_post'] -dfProfile_con['MAS_pre']
diff_BS_con = dfProfile_con['BS_post'] - dfProfile_con['BS_pre']

diff_MAS_int = dfProfile_int['MAS_post'] - dfProfile_int['MAS_pre']
diff_BS_int = dfProfile_int['BS_post'] - dfProfile_int['BS_pre']



print()
print()
# หาความแตกแต่างภายในกลุ่ม ก่อน-หลังได้รับการรักษา
study.distribution(dfProfile_con['MAS_pre'], dfProfile_con['MAS_post'])
pvalue_MAS_con = study.intradiff()
if pvalue_MAS_con >= 0.05 : 
    print('There is not significant difference of MAS score after treatment in control group')
elif pvalue_MAS_con < 0.05 :
    print('There is significant difference of MAS score after treatment in control group')
print('p-value = ', round(pvalue_MAS_con, 2))

study.distribution(dfProfile_con['BS_pre'], dfProfile_con['BS_post'])
pvalue_BS_con = study.intradiff()
if pvalue_BS_con >= 0.05 : 
    print('There is not significant difference of BS score after treatment in control group')
elif pvalue_BS_con < 0.05 :
    print('There is significant difference of BS score after treatment in control group')
print('p-value = ', round(pvalue_BS_con, 2))


study.distribution(dfProfile_int['MAS_pre'], dfProfile_int['MAS_post'])
pvalue_MAS_int = study.intradiff()
if pvalue_MAS_int >= 0.05 : 
    print('There is not significant difference of MAS score after treatment in intervention group')
elif pvalue_MAS_int < 0.05 :
    print('There is significant difference of MAS score after treatment in intervention group')
print('p-value = ', round(pvalue_MAS_int, 2))


study.distribution(dfProfile_int['BS_pre'], dfProfile_int['BS_post'])
pvalue_BS_int = study.intradiff()
if pvalue_BS_int >= 0.05 : 
    print('There is not significant difference of BS score after treatment in intervention group')
elif pvalue_BS_int < 0.05 :
    print('There is significant difference of BS score after treatment in intervention group')
print('p-value = ', round(pvalue_BS_int, 2))


print()
print()
# เทียบ MAS, BS ระหว่างสองกลุ่ม ** อันนี้ต้องเอา ผลต่างมาเทียบกัน
study.distribution(diff_MAS_con, diff_MAS_int)
pvalue_MAS = study.interdiff()
if pvalue_MAS >= 0.05 : 
    print('There is not significant difference of MAS score between control and intervention group')
elif pvalue_MAS < 0.05 :
    print('There is significant difference of MAS score between control and intervention group')
print('Mean difference of MAS between two comparison groups', np.mean(diff_MAS_int) - np.mean(diff_MAS_con))
print('p-value = ', round(pvalue_MAS, 2))

study.distribution(diff_BS_con, diff_BS_int)
pvalue_BS = study.interdiff()
if pvalue_BS >= 0.05 : 
    print('There is not significant difference of BS score between control and intervention group')
elif pvalue_BS < 0.05 :
    print('There is significant difference of BS score between control and intervention group')
print('Mean difference of BS between two comparison groups', np.mean(diff_BS_int) - np.mean(diff_BS_con))
print('p-value = ', round(pvalue_BS, 2))


diff_MAS_con.hist(bins = 8, alpha = 0.5, label = 'Control group')
diff_MAS_int.hist(bins = 8, alpha = 0.5, label = 'Experimental group')
mean_diff_con_MAS = diff_BS_con.mean()
mean_diff_exp_MAS = diff_BS_int.mean()
plt.title('Distribution of MAS difference between in both groups.')
plt.xlabel('MAS difference between pre-intervention and post-intervention')
plt.axvline(mean_diff_con_MAS, color = 'navy', linestyle = 'dashed', linewidth = 1, label = 'mean difference of control group')
plt.axvline(mean_diff_exp_MAS, color = 'red', linestyle = 'dashed', linewidth = 1, label = 'mean difference of experimental group')
plt.legend()
plt.show()


diff_BS_con.hist(bins = 8, alpha = 0.5, label = 'Control group')
diff_BS_int.hist(bins = 8, alpha = 0.5, label = 'Experimental group')
mean_diff_con_BS = diff_BS_con.mean()
mean_diff_exp_BS = diff_BS_int.mean()
plt.title('Distribution of BS difference between in both groups.')
plt.xlabel('BS difference between pre-intervention and post-intervention')
plt.axvline(mean_diff_con_BS, color = 'navy', linestyle = 'dashed', linewidth = 1, label = 'mean difference of control group')
plt.axvline(mean_diff_exp_BS, color = 'red', linestyle = 'dashed', linewidth = 1, label = 'mean difference of experimental group')
plt.legend()
plt.show()

