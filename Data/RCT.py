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
age_Con = np.round(np.random.normal(50, 2, ss)).astype(int)
age_Int = np.round(np.random.normal(50, 2, ss)).astype(int)

onset_Con = np.round(np.random.normal(12,2, ss)).astype(int)
onset_Int = np.round(np.random.normal(12,2, ss)).astype(int)


vol_Con = np.random.normal(15,2, ss)
vol_Int = np.random.normal(15,2, ss)

# baseline clinical score

MAS_preControl = np.random.choice([0,1,2,3,4,5], ss, p = [0.1,0.1,0.1,0.3,0.4,0.0])
MAS_postControl = np.random.choice([0,1,2,3,4,5], ss, p = [0.2,0.3,0.3,0.1,0.1,0.0])
MAS_preInt = np.random.choice([0,1,2,3,4,5], ss, p = [0.1,0.1,0.1,0.3,0.4,0.0])
MAS_postInt = np.random.choice([0,1,2,3,4,5], ss, p = [0.2,0.3,0.3,0.2,0.0,0.0])

BS_preControl = np.random.choice([1,2,3,4,5,6], ss, p = [0.2,0.3,0.2,0.1,0.1,0.1])
BS_postControl = np.random.choice([1,2,3,4,5,6], ss, p = [0.0,0.2,0.2,0.2,0.2,0.2])
BS_preInt = np.random.choice([1,2,3,4,5,6], ss, p = [0.2,0.3,0.2,0.1,0.1,0.1])
BS_postInt = np.random.choice([1,2,3,4,5,6], ss, p = [0.0,0.0,0.2,0.2,0.3,0.3])

ProfileData = {'Patients ID':ID_np , 'Age Control':age_Con, 'Age Intervention':age_Int, 'Onset Control':onset_Con, 'Onset Intervention':onset_Int,
               'Vol(cm3) Control':vol_Con, 'Vol(cm3) Intervention':vol_Int}

dfProfile = pd.DataFrame(ProfileData)
dfProfile = dfProfile.set_index('Patients ID')
print(dfProfile)
print(dfProfile.describe())

ClinicalData = {'Patients ID':ID_np, 'MAS pre-control':MAS_preControl, 'MAS post-control':MAS_postControl,
                'MAS pre-intervention':MAS_preInt, 'MAS post-intervention':MAS_postInt,
                'BS pre-control':BS_preControl, 'BS post-control':BS_postControl,
                'BS pre-intervention':BS_preInt, 'BS post_intervention':BS_postInt}

dfClinical = pd.DataFrame(ClinicalData)
dfClinical = dfClinical.set_index('Patients ID')
print(dfClinical)
print(dfClinical.describe())






# profile comparison
# compare ages between group
research.distribution(dfProfile['Age Control'], dfProfile['Age Intervention'])
pvalue = research.interdiff()
if pvalue >= 0.05 : 
    print('The difference in age between the two groups is not statistically significant, p-value{}'.format(pvalue))
else :
    print('The difference in age between the two groups is statistically significant, p-value{}'.format(pvalue))
#compare onset between group
research.distribution(dfProfile['Onset Control'], dfProfile['Onset Intervention'])
pvalue = research.interdiff()
if pvalue >= 0.05 : 
    print('The difference in onset between the two groups is not statistically significant, p-value {}'.format(pvalue))
else :
    print('The difference in onset between the two groups is statistically significant, p-value {}'.format(pvalue))
#compare volume between group
research.distribution(dfProfile['Vol(cm3) Control'], dfProfile['Vol(cm3) Intervention'])
pvalue = research.interdiff()
if pvalue >= 0.05 :
    print('The difference in lesion volume between the two groups is not statistically significant, p-value {}'.format(pvalue))
else :
    print('The difference in lesion volume between the two groups is statistically significant, p-value {}'.format(pvalue))

# clinical baseline comparison
# MAS
research.distribution(dfClinical['MAS pre-control'], dfClinical['MAS pre-intervention'])
pvalue = research.interdiff()
if pvalue >= 0.05 : 
    print('The difference in MAS baseline between the two groups is not statistically significant, p-value{}'.format(pvalue))
else :
    print('The difference in MAS baseline between the two groups is statistically significant, p-value{}'.format(pvalue))

#BS
research.distribution(dfClinical['BS pre-control'], dfClinical['BS pre-intervention'])
pvalue = research.interdiff()
if pvalue >= 0.05 : 
    print('The difference in BS baseline between the two groups is not statistically significant, p-value{}'.format(pvalue))
else :
    print('The difference in BS baseline between the two groups is statistically significant, p-value{}'.format(pvalue))


# Intragroup comparison 

# MAS : conventional therapy 
research.distribution(dfClinical['MAS pre-control'], dfClinical['MAS post-control'])
pvalue = research.intradiff()
if pvalue < 0.05 : 
    print('The MAS score of control group showed significant improvement after receiving conventional therapy, p-value {}'.format(pvalue))
else : 
    print('The MAS score of control group showed no significant improvement after receiving conventional therapy, p-value {}'.format(pvalue))

# MAS : interventional therapy
research.distribution(dfClinical['MAS pre-intervention'], dfClinical['MAS post-intervention'])
pvalue = research.intradiff()
if pvalue < 0.05 : 
    print('The MAS score of intervention group showed significant improvement after receiving interventional therapy, p-value {}'.format(pvalue))
else : 
    print('The MAS score of intervention group showed no significant improvement after receiving interventional therapy, p-value {}'.format(pvalue))

# BS : conventional therapy 
research.distribution(dfClinical['BS pre-control'], dfClinical['BS post-control'])
pvalue = research.intradiff()
if pvalue < 0.05 : 
    print('The BS score of control group showed significant improvement after receiving conventional therapy, p-value {}'.format(pvalue))
else : 
    print('The BS score of control group showed no significant improvement after receiving conventional therapy, p-value {}'.format(pvalue))

# BS : interventional therapy 
research.distribution(dfClinical['BS pre-intervention'], dfClinical['BS post_intervention'])
pvalue = research.intradiff()
if pvalue < 0.05 : 
    print('The BS score of interventional group showed significant improvement after receiving interventional therapy, p-value {}'.format(pvalue))
else : 
    print('The BS score of interventional group showed no significant improvement after receiving interventional therapy, p-value {}'.format(pvalue))

# Intergroup comparison for efficacy

# MAS
research.distribution(dfClinical['MAS post-control'], dfClinical['MAS post-intervention'])
pvalue = research.interdiff() 
if pvalue < 0.05 : 
    print('The MAS score of interventional group showed significant improvement compared with conventional therapy, p-value {}'.format(pvalue))
else :
    print('The MAS score of interventional group showed no significant improvement compared with conventional therapy, p-value {}'.format(pvalue))

#BS 
research.distribution(dfClinical['BS post-control'], dfClinical['BS post_intervention'])
pvalue = research.interdiff()
if pvalue < 0.05 : 
    print('The BS score of interventional group showed significant improvement compared with conventional therapy, p-value {}'.format(pvalue))
else :
    print('The BS score of interventional group showed no significant improvement compared with conventional therapy, p-value {}'.format(pvalue))