# Dictionary = 'country':sub-dictionary
# Sub-dictionary = capital , population (millions)
# Use objected oriented programming for demography editing
    # add vietnam into ASEAN, vietnam = {'capital':'hanoi', 'population': 87.9}
    # add GDP per capita into subdictionary
# Import Numpy for array creation
# Import matplotlib for display any relationships graph 



class demography :

    def __init__(self, association) :
        self.association = association
    
    def member(self) :
        self.member = self.association
        
    
    def addmember(self) : 
        newmember = input('New member country : ')
        capital = input('capital : ')
        population = float(input('population (millions) : '))
        subdict = {}
        subdict['capital'] = capital
        subdict['population'] = population
        self.member[newmember] = subdict
        print(newmember, 'is qualified to be the new member of the associaiton.')
        

    def addinform(self) :
        inform = input('Which information you need to add? : ')
        for country in self.member :
            detail = float(input(country + '='))
            self.member[country][inform] = detail
        print('The association consists of ', self.member)
        return inform, self.member




ASEAN = {'brunei':{'capital':'begawan', 'population':0.4 },
         'cambodia':{'capital':'phnompenh', 'population':15},
         'indonesia':{'capital':'jakarta','population':238},
         'lao':{'capital':'vientiane', 'population':6.3 },
         'malaysia':{'capital':'kualalumpur', 'population':28.9 },
         'myanmar':{'capital':'naypyitaw', 'population':54 },
         'philippines':{'capital':'manila', 'population':95.7 },
         'singapore':{'capital':'singapore', 'population':6.3 },
         'thailand':{'capital':'bangkok', 'population':69.5 }}

association = demography(ASEAN)
association.member()

# add vietnam into ASEAN
# vietnam = {'capital':'hanoi', 'population': 87.9}
association.addmember()

# add GDP per capita : https://www.investerest.co/economy/thailands-gdp/
# GDP แบบต่อหัว หรือ GDP per capita โดยมีหน่วยเป็นดอลลาร์สหรัฐ ($) คือ สิงค์โปร (66,263.42) บรูไน (33,979.37) มาเลเซีย (11,124.67) ไทย (7,808.66) อินโดนีเซีย (4,224.98) เวียดนาม (3,742.86) ฟิลิปปินส์ (3,492.07) ลาว (2625.61) กัมพูชา (1647.02) และ เมียนมาร์ (1,246.32)

inform, ASEAN = association.addinform()

# import numpy for array establishing 
# X = countries , Y = GDPperCap , scatter size = population
import numpy as np

countries = []
for i in ASEAN :
    countries.append(i)
print(countries)
countries_np = np.array(countries)


GDPperCap = []
for i in ASEAN :
    GDP = ASEAN[i][inform]
    GDPperCap.append(GDP)
print(GDPperCap)
GDPperCap_np = np.array(GDPperCap)


population = []
for i in ASEAN :
    pop = ASEAN[i]['population']
    population.append(pop)
population_np = np.array(population) 


data = np.column_stack((countries_np, GDPperCap_np))
print(data)


import matplotlib.pyplot as plt 

plt.xlabel('Countries')
plt.ylabel('GDPperCapita')
plt.title('ASEAN GDP')
plt.bar(countries_np, GDPperCap_np)
plt.show()




