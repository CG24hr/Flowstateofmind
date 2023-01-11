import numpy as np 
import pandas as pd

# input เฉพาะ columns ที่ต้องการหาความสัมพันธ์กัน
dict = {}
columns = []
count = 0
N = int(input('Number of columns : '))
while count < N :
    col = input('column ' + str(count+1) + ' : ')
    columns.append(col)
    count = count + 1
print(columns)

n = int(input('Number of data : '))
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

df = pd.DataFrame(dict)
print(df)

table = pd.crosstab(df.iloc[:, 0], df.iloc[:, 1])
table = table.sort_index(axis = 0, ascending = True)
table = table.sort_index(axis = 1, ascending = True)
print(table)