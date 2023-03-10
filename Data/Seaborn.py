import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


temperature = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
ice_cream_sales = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
sns.scatterplot(x = temperature, y = ice_cream_sales) # กรณีที่เป็น dataframe จะเป็น (x = 'column1', y = 'column2', data = df)
plt.show()

grades = ['A', 'B', 'C', 'D', 'F', 'A', 'C', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'C', 'D', 'A', 'B', 'A', 'F', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'B', 'B', 'C', 'A', 'B', 'A', 'C', 'C', 'B', 'B', 'D', 'F', 'B', 'C', 'B', 'A', 'B', 'A', 'B', 'C', 'A', 'B']
sns.countplot(y = grades)
plt.show()
sns.countplot(x = grades)
plt.show()

Age_BP = {'Age': [30, 35, 40, 45, 50, 55, 60, 65, 70, 75],
        'Blood Pressure': [120, 130, 140, 150, 160, 170, 180, 190, 200, 210],
        'Gender': ['M', 'F', 'F', 'M', 'F', 'F', 'M', 'M', 'F', 'M'],
        'DM' : ['True', 'False', 'False', 'True', 'False', 'False', 'True', 'False', 'True', 'False'],
        'BMI': [22, 24, 26, 28, 30, 32, 34, 36, 38, 40]
        }
Age_BP = pd.DataFrame(Age_BP)
hue_colors = {'M':'Navy', 'F':'Pink'}
sns.scatterplot(x = 'Age', y = 'Blood Pressure', data = Age_BP, hue = 'Gender', palette = hue_colors, style = 'Gender')
sns.relplot(x = 'Age', y = 'Blood Pressure', kind = 'scatter', data = Age_BP, hue = 'Gender', style = 'Gender', size = 'BMI')
plt.show()
 
#sns.relplot จะช่วยแยกแต่ละ hue ออกมาเป็น subplot
sns.relplot(x = 'Age', y = 'Blood Pressure', kind = 'scatter', data = Age_BP, col = 'Gender', row = 'DM') # สามารถใช้ argument row หรือ col อย่างใดอย่างหนึ่งก็ได้
plt.show()


data = {'Gender': ['M', 'F', 'F', 'M', 'M', 'F', 'M', 'F', 'F', 'M',
                  'F', 'M', 'M', 'F', 'M', 'M', 'F', 'F', 'M', 'F'],
        'Smoker': ['Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'No', 'Yes', 'No',
                  'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'No', 'Yes', 'No']}
Sex_Smoke = pd.DataFrame(data)
sns.countplot(x = 'Smoker', data = Sex_Smoke, hue = 'Gender', hue_order=['F', 'M'])
plt.show()
