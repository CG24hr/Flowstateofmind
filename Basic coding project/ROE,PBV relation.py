#สร้าง project matplotlib.pyplot โดยสร้างความสัมพันธ์ระหว่าง ROE(แกน x) และ PBV ratio(แกนY) 
# โดยนำค่า 5 ปีของหุ้น มา plot
#Example apple 2016-2020 

def ROE () :
    FiveYearsROE =[]
    #ไม่ควรมีบรรทัดว่างในไฟล์.txt 
    with open('D:\\Users\\Desktop\\Python code\\GitHub\\Flowstateofmind\\Basic coding project\\financialstatement.txt') as statement :
        for list in statement :
            financialList = list.split()
            FiveYearsROE.append(float(financialList[2]))
    return FiveYearsROE

def PBV () :
    FiveYearsPBV = []
    with open('D:\\Users\\Desktop\\Python code\\GitHub\\Flowstateofmind\\Basic coding project\\financialstatement.txt') as statement : 
        for list in statement :
            financialList = list.split()
            FiveYearsPBV.append(float(financialList[4]))
    return FiveYearsPBV


averageROE = sum(ROE()) / len(ROE())
print('Average 5 years ROE is', averageROE, '%' )
averagePBV = sum(PBV()) / len(PBV())
print('Average 5 years PBVratio is', averagePBV )


print(ROE())
print(PBV())

import matplotlib.pyplot as plt 
plt.scatter(ROE() , PBV())
plt.show()

