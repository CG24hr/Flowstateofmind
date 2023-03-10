import pandas as pd
import statsmodels.api as sm
import numpy as np 
# Load the data into a pandas DataFrame
bmi = np.random.normal(30, 5, 1000)
hba1c = np.random.normal(8, 1, 1000)
abi = np.random.normal(0.8, 0.1, 1000)
amp = np.random.choice([True, False], p = [0.8, 0.2], size = 1000)
dict = {'BMI':bmi, 'HbA1c':hba1c, 'ABI':abi, 'limb amputation':amp}
df = pd.DataFrame(dict)

# Define the independent and dependent variables
X = df[['BMI', 'HbA1c', 'ABI']]
y = df['limb amputation']

X = sm.add_constant(X)

# Fit the logistic regression model
model = sm.Logit(y, X)  # sm.OLS(y, x) กรณี multiple linear regression
result = model.fit()

# Print the summary of the model
print(result.summary())


stroke = pd.read_csv('D:\\Users\\Desktop\\Python code\\GitHub\\Flowstateofmind\\Data\\csv\\healthcare-dataset-stroke-data.csv')
stroke = stroke.dropna()
print(stroke)

map_dict = {'formerly smoked':1, 'smokes':1, 'never smoked':0, 'Unknown':0}
stroke['smoking_status'] = stroke['smoking_status'].map(map_dict)
print(stroke)

X = stroke[['avg_glucose_level', 'bmi', 'hypertension', 'smoking_status']]
Y = stroke['stroke']

X = sm.add_constant(X)
model = sm.Logit(Y, X)
result = model.fit()
result = result.summary2()
print(result)
print(result.tables[1])
# ส่วนการคิด Odd ratios คือการเอา coefficient มา exponentiate -> np.exp(coef.) + ** อย่าลืมเอา upper & lower limit ของ 95% CI มา exponentiate ด้วย เพราะนั่นคือค่าของ coefficient ยังไม่ใช่ของ Odd ratios 
