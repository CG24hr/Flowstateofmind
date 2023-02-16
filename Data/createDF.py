import numpy as np 
import pandas as pd

class study : 

    def createDataframe(self) :
        # input เฉพาะ columns ที่ต้องการหาความสัมพันธ์กัน
        print('For screening/diagnostic test, Input 2 columns of Screening and Gold standard')
        print('Input 1 : if test shows positive, 0 : if test shows negative')

        dict = {}
        columns = []
        count = 0
        N = int(input('Number of columns : '))
        while count < N :
            col = input('column ' + str(count+1) + ' : ')
            columns.append(col)
            count = count + 1
        print(columns)

        n = int(input('Number of patients : '))
        count = 0
        for i in columns : 
            list = []
            while count < n :
                data = input('rows ' + str(count+1) + ' ' + i + ' : ')
                list.append(data)
                count = count + 1
                dict[i] = np.array(list)
            count = 0 
        print(dict)

        self.df = pd.DataFrame(dict)
        print(self.df)

    def Screening(self) : 
        # Screening/diagnostic test 
        table = pd.crosstab(self.df.iloc[:, 0], self.df.iloc[:, 1])
        table = table.sort_index(axis = 0, ascending = False)
        table = table.sort_index(axis = 1, ascending = False)
        print(table)
        ppv = table.iloc[0, 0] / (table.iloc[0, 0] + table.iloc[0, 1])
        npv = table.iloc[1, 1] / (table.iloc[1, 0] + table.iloc[1, 1])
        sensitivity = table.iloc[0, 0] / (table.iloc[0, 0] + table.iloc[1, 0])
        specificity = table.iloc[1, 1] / (table.iloc[1, 1] + table.iloc[0, 1])
        print('ppv = ', ppv)
        print('npv = ', npv)
        print('sensitivity = ', sensitivity)
        print('specificity = ', specificity)


Screening = study()
Screening.createDataframe()
Screening.Screening()
