# scatter relationship between Age and Income in EV users
# create Age & Income list, lenght = 100 , แล้วเรียงลำดับจากน้อยไปมาก
# ใช้ numpy เปลี่ยน Bath เป็น Dollars
# ใช้ np.column_stack แล้วจบด้วยนำ column 0 เป็นแกน X , column 1 เป็น แกน Y
# axis X = annual income[Bath], Y = Age, each scatter size = population
# แสดงผล
    #  รายได้เฉลี่ยของผู้ใช้ EV 
    #  อายุเฉลี่ยของผู้ใช้ EV 
    #  จำนวนผู้ใช้ EV ทั้งหมดในประเทศไทย
# แสดงผล population 

import numpy as np

# ใช้ module random สร้างชุดข้อมุลผ่าน loop ขึ้นมาแล้วจัดเรียงข้อมูลจากน้อยไปมาก
import random
n = 20

Age = []
for i in range(n) :
    age = random.randrange(20,61)
    Age.append(age)
Age = sorted(Age)
Age_np = np.array(Age)

Income = []
for i in range(n) :
    income = random.randrange(15000,200001)
    Income.append(income)
Income = sorted(Income)
Income_np = np.array(Income)
# เปลี่ยน Income จากหน่วย Bath เป็น Dollars
Income_np_dollars = Income_np * 0.029

# Population ของคนแต่ละอายุ
Population = []
for i in Age_np :
    pop = random.randrange(100,1001)
    Population.append(pop)
Population_np = np.array(Population)


# แสดงผลค่าต่างๆ
EVusers = np.column_stack((Age_np, Income_np_dollars))
print(EVusers)
print('Total EV users in Thailand is ', sum(Population_np))
print('Average age of EV users in Thailand is ', np.mean(EVusers[:, 0]))
print('Average annual income of EV users in Thailand is ', np.mean(EVusers[:, 1]), 'dollars')



col = ['red','red','red','red','orange','orange','orange','orange','green','green','green','green','purple','purple','purple','purple','yellow','yellow','yellow','yellow']

import matplotlib.pyplot as plt 

plt.xlabel('Age')
plt.ylabel('Population')
plt.bar(EVusers[:, 0], Population_np)
plt.show()

plt.title('Relationships between age and income of EV users in Thailand')
plt.xlabel('Age')
plt.ylabel('Income(Dollars)')
plt.scatter(EVusers[:, 0], EVusers[:, 1], s = Population_np, alpha = 0.8, c = col)
plt.text(35, 2000, 'A')
plt.text(45, 3500, 'B')
plt.show()

