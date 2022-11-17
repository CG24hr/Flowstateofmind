#สร้าง function แยกแต่ละ parameter (eg. ROE,PER,PBV,payroutratio) 
# นำมาประเมินมูลค่าหุ้น
#import matplotlib.pyplot as plt มาหาความสัมพันธ์ของแต่ละ parameter


def ROE(fiscalyears) :
    year = 0
    annualROE =[]
    while year < fiscalyears :
            year = year + 1 
            ROE = float(input('Enter annual ROE% :'))
            annualROE.append(ROE)
    averageROE = sum(annualROE) / len(annualROE)
    print(fiscalyears, 'years ROEratio = ', annualROE)
    print('Average ROE% in' , fiscalyears , 'years is' , averageROE , ('%'))
    return annualROE , averageROE

def PER(fiscalyears) :
    year = 0
    annualPER =[]
    while year < fiscalyears :
            year = year + 1 
            PER = float(input('Enter annual P/E ratio :'))
            annualPER.append(PER)
    averagePER = sum(annualPER) / len(annualPER)
    print(fiscalyears, 'years P/E ratio = ', annualPER)
    print('Average P/Eratio in' , fiscalyears , 'years is' , averagePER , '%'  )
    return annualPER , averagePER

def PBV(fiscalyears) :
    year = 0
    annualPBV =[]
    while year < fiscalyears :
            year = year + 1 
            PBV = float(input('Enter annual P/BV ratio :'))
            annualPBV.append(PBV)
    averagePBV = sum(annualPBV) / len(annualPBV)
    print(fiscalyears, 'years PBV ratio = ', annualPBV)
    print('Average P/BV ratio in' , fiscalyears , 'years is' , averagePBV )
    return annualPBV , averagePBV 

def payoutratio(fiscalyears) :
    year = 0
    annualpayoutratio =[]
    while year < fiscalyears :
            year = year + 1 
            PBV = float(input('Enter annual payout ratio(%):'))
            annualpayoutratio.append(PBV)
    averagepayoutratio = sum(annualpayoutratio) / len(annualpayoutratio)
    print(fiscalyears, 'years payout ratio is = ', annualpayoutratio , '%')
    print('Average payout ratio in' , fiscalyears , 'years is' , averagepayoutratio , '%')
    return annualpayoutratio , averagepayoutratio 





#input ข้อมูลให้ function และกำหนดตัวแปรเพื่อรับ output จาก function
fiscalyears = int(input('Enter number of fiscal years :'))
ROElist , averageROE = ROE(fiscalyears)
PERlist , averagePER = PER(fiscalyears)
PBVlist , averagePBV = PBV(fiscalyears)
annualpayoutratio , averagepayoutratio  = payoutratio(fiscalyears)


#หาความสัมพันธ์ระหว้าง P/BV ratio และ ROE(%)
import matplotlib.pyplot as plt
plt.xlabel('ROE(%)')
plt.ylabel('P/BVratio') 
plt.scatter(ROElist,PBVlist)
plt.show()


#Buffetology valuation
#หา ราคาที่เหมาะสม ในอีก t ปี

eps = float(input('Enter recent earning per share :'))
equitypershare = float(input('Enter recent equity per share :'))
if eps > 0 and equitypershare > 0 :
    t = int(input('Enter number of long term years : '))
    #หาอัตราการเติบโตของส่วนผู้ถือหุ้น
    g = ( 1 - averagepayoutratio/100 ) * averageROE
    print('Predictive average equity per share growth is' , g , '% per year.')
    #หาส่วนของผู้ถือหุ้นในอีก t ปีข้างหน้า
    Tyearsequitypershare = equitypershare * ((1 + g/100)**t)
    print('Predictive' , t , 'years equity per share is' , Tyearsequitypershare)
    #หาราคาที่เหมาะสมในอีก t ปีข้างหน้า
    TyearsEPS = (averageROE/100) * Tyearsequitypershare
    Tyearsfairvalue =  averagePER * TyearsEPS
    print('Predictive earning per share next' , t , 'years is' , TyearsEPS )
    print('Predictive fair value next' , t , 'years is' , Tyearsfairvalue )
else :
    print('Please check your information.')


#คำนวนหาผลตอบแทนย้อนหลังในอีก t ปี
recentprice = float(input('Enter recent stock price :'))
r = (((Tyearsfairvalue / recentprice)**(1/t)) - 1) * 100
print('Predictive' , t , 'years annual return rate is' , r , '%')

