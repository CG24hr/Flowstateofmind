# คิดภาษีแบบชั้นบันได เฉพาะเงินได้ประเภทที่ 1 
# ref : https://www.itax.in.th/pedia/%e0%b8%84%e0%b9%88%e0%b8%b2%e0%b8%a5%e0%b8%94%e0%b8%ab%e0%b8%a2%e0%b9%88%e0%b8%ad%e0%b8%99/
class personal_incomeTax  :

    def __init__ (self,income) :
        self.income = income
    # หักค่าใช้จ่าย แบบเหมา 50% แต่ไม่เกิน 100000

    def expenses(self) :
        if self.income * 0.5 > 100000 :
            self.expenses = 100000    
        else : 
            self.expenses = self.income * 0.5    
        self.income = self.income - self.expenses 
        
        
    # ลดหย่อนส่วนบุคคลธรรมดา 60000
    def individual (self) :
        self.income = self.income - 60000
        

    # หักค่าลดหย่อนอื่นๆ 

    def marry (self) : #แต่งงานแล้วหักได้ 60000
        marry = input('Are you married ? <Y/N> : ')
        if marry == 'Y' :
            self.income = self.income - 60000
        elif marry == 'N' :
            self.income = self.income 
        

    def child (self) : #บุตรคนละ 30000
        child = int(input('Enter number of your child :'))
        self.income = self.income - (child * 30000)
       

    def parent (self) : # บิดามารดาคนละ 30000 หากอายุเกิน 60 และไม่ได้มีรายได้
        parent = input('Do you have a duty to take care of your parent ? <Y/N> : ')
        if parent == 'Y' :
            N = int(input('Only one or Both ? <1/2> :'))
            if N == 1 or N == 2 :
                self.income = self.income - (N*30000)
            else : 
                None
        else :
            self.income = self.income 
       

    def impair (self) : # พิการหรือทุพพลภาพ หักได้ 60000
        impair = input('Do you have any impairments or disabilities ? <Y/N> :')
        if impair == 'Y' :
            self.income = self.income - 60000
        else :
            None
      

    def ANC (self) : # ฝากครรภ์ลดหย่อนได้ 60000
        ANC = input('Are you getting antenatal care ? <Y/N> : ')
        if ANC == 'Y' :
            ANCexpense = int(input('Enter your expenditure for antenatal care :'))
            if ANC == 'Y' and 0 <= ANCexpense <= 60000 :
                self.income = self.income - ANCexpense
            elif ANC == 'Y' and ANCexpense > 60000 :
                self.income = self.income - 60000
            else : 
                None
        else :
            None
        


    def insurance (self) : # รวมประกันชีวิตทั่วไป และเงินฝากแบบมีประกันชีวิต ไม่เกิน 100000
        insurance = int(input('Enter your expenditure for your insurance :'))
        if insurance > 100000 :
            self.income = self.income - 100000
        elif insurance >= 0 :
            self.income = self.income - insurance
       

    def Pinsurance (self) : # ประกันชีวิตบิดามารดา รวมกันไม่เกิน 15000
        Pinsurance = int(input('Enter your expenditure for your parent insurance :'))
        if Pinsurance > 15000 :
            self.income = self.income - 15000
        elif Pinsurance >= 0 :
            self.income = self.income - Pinsurance
        

    def provident (self,income) : # กองทุนสำรองเลี้ยงชีพ หรือ กบข. ไม่เกิน 15 % ของเงินเดือน  
        provident = int(input('Enter your provident fund asset :'))
        if provident > 0.15 * income :
            provident = 0.15 * income
            self.income = self.income - provident 
        elif provident >= 0 :
            self.income = self.income - provident
        self.provident = provident
        

    def RMF (self, income) : # กองทุน RMF ไม่เกิน 30 % ของเงินได้ที่ต้องเสียภาษี และรวมกับ provident ไม่เกิน 5 แสน
        RMF = int(input('Enter your RMF :'))
        if RMF > 0.30 * income :
            RMF = 0.3 * income 
            self.income = self.income - RMF
        elif RMF >= 0 :
            self.income = self.income - RMF
        self.RMF = RMF 
        

    def annuity (self, income) : # ประกันชีวิตแบบบำนาญ ไม่เกิน 15 % ของเงินได้ที่ต้องเสียภาษี และไม่เกิน 2 แสน และรวมกับ provident + RMF ไม่เกิน 5 แสน
        annuity = int(input('Enter your annuity :'))
        if annuity > 0.15 * income :
            annuity = 0.15 * income
            self.income = self.income - annuity 
            if annuity > 200000 :
                self.income = self.income - 200000
        elif annuity >= 0 and annuity > 200000 :
            self.income = self.income - 200000
        elif annuity >= 0 :
            self.income = self.income - annuity
        self.annuity = annuity
        
    
    def social (self) : # กองทุนประกันสังคม ไม่เกิน 9000 บาท
        social = int(input('Enter your social security fund :'))
        if social > 9000 :
            self.income = self.income - 9000
        elif 0 <= social <= 9000 :
            self.income = self.income - social
        
            
    def national (self) : # กองทุนการออมแห่งชาติ ไม่เกิน 13200 และ รวมกับ provident + RMF + annuity ไม่เกิน 500000
        national = int(input('Enter your national saving fund :'))
        if national > 13200 :
            self.income = self.income - 13200
        elif 0 <= national <= 13200 :
            self.income = self.income - national
        self.national = national
        

    def SSF (self, income) : # กองทุน SSF ไม่เกิน 30 % ของเงินได้ที่ต้องเสียภาษี และไม่เกิน 200000 และรวมกับ provident + RMF + annuity + nationalsavingfund ไม่เกิน 500000
        SSF = int(input('Enter your SSF :'))
        if SSF > 0.30 * income :
            SSF = 0.30 * income
            self.income = self.income - SSF 
            if SSF > 200000 :
                self.income = self.income - 200000
        elif SSF >= 0 and SSF >= 200000 :
            self.income = self.income - 200000
        elif SSF >= 0 :
            self.income = self.income - SSF 
        self.SSF = SSF 
        

    def interest (self) : # ดอกเบี้ยที่อยู่อาศัย ไม่เกิน 1 แสน
        interest = int(input('Enter residential interest :'))
        if interest > 100000 :
            self.income = self.income - 100000
        elif 0 <= interest <= 100000 :
            self.income = self.income - interest
        

    def politicalparty (self) : # เงินบริจาคพรรคการเมือง ไม่เกิน 10000
        politicalparty = int(input('Enter political party donation :'))
        if politicalparty > 10000 :
            self.income = self.income - 10000
        elif 0 <= politicalparty <= 10000 :
            self.income = self.income - politicalparty
        

    def socialdonate (self) : # หัก 2 เท่า ของเงินบริจาคที่จ่าย แต่ไม่เกิน 10 % ของเงินได้หลังหักค่าลดหย่อน 
        socialdonate = int(input('Enter your social donation including education, sport, social developement, and public hospital :'))
        if socialdonate > 0.1 * self.income :
            socialdonate = 0.1 * self.income
            self.income = self.income - socialdonate
        elif socialdonate <= 0.1 * self.income and socialdonate >= 0 :
            self.income = self.income - (socialdonate * 2)
        

    def generaldonate (self) : # เงินบริจาคทั่วไป ไม่เกิน 10 % ของเงินได้หลังหักค่ารถหย่อน 
        generaldonate = int(input('Enter general donation :'))
        if generaldonate > 0.1 * self.income :
            generaldonate = 0.1 * self.income
            self.income = self.income - generaldonate
        elif generaldonate <= 0.1 * self.income and generaldonate >= 0 :
            self.income = self.income - generaldonate 
        



    # นำรายได้ทั้งปีของบุคลากรแต่ละคนมาคำนวณภาษีตามขั้นบันได แล้วนำมาหักกับภาษี ณ ที่จ่าย (ภาษีที่ต้องจ่ายทั้งปี / จำนวนงวดที่จ่ายเงินเดือน)
    def ladder (self) :
        if self.income <= 150000 :
            incomeTax = 0
        elif 150001 <= self.income <= 300000 :
            incomeTax = self.income*0.05
        elif 300001 <= self.income <= 500000 :
            incomeTax = ((self.income-300000)*0.10) + (150000*0.05) 
        elif 500001 <= self.income <= 750000 :
            incomeTax = ((self.income-500000)*0.15) + (200000*0.1) + (150000*0.05) 
        elif 750001 <= self.income <= 1000000 :
            incomeTax = ((self.income-750000)*0.20) + (250000*0.15) + (200000*0.10) + (150000*0.05) 
        elif 1000001 <= self.income <= 2000000 :
            incomeTax = ((self.income-1000000)*0.25) + (250000*0.15) + (250000*0.15) + (200000*0.10) + (150000*0.05) 
        elif 2000000 <= self.income <= 5000000 :
            incomeTax = ((self.income-2000000)*0.30) + (1000000*0.25) + (250000*0.15) + (250000*0.15) + (200000*0.10) + (150000*0.05) 
        elif self.income > 5000000 :
            incomeTax = ((self.income-5000000)*0.35) + (3000000*0.30) + (1000000*0.25) + (250000*0.15) + (250000*0.15) + (200000*0.10) + (150000*0.05)

        self.incomeTax = incomeTax

    def showdata(self) :
        if self.provident + self.RMF + self.annuity + self.national + self.SSF > 500000 : # เช็คว่ากรณีที่รวมกันเกิน 5 แสน เป็นจริงไหม ถ้าใช่ถือว่าเป็นโมฆะ
            print('The summary of your provident fund, SSF/RMF, annuity, and national saving fund is over 500000, Please check your information.')
        else :
            if self.incomeTax <= 0 :
                print('Taxpayer status : You are not candidate for filing.')
            elif self.incomeTax > 0 :
                print('Your total income tax is', self.incomeTax)


income = int(input('Enter your income :'))
employee = personal_incomeTax(income)
employee.expenses()
employee.individual()
employee.marry()
employee.child()
employee.parent()
employee.impair()
employee.ANC()
employee.insurance()
employee.Pinsurance()
employee.provident(income)
employee.RMF(income)
employee.annuity(income)
employee.social()
employee.national()
employee.SSF(income)
employee.interest()
employee.politicalparty()
employee.socialdonate()
employee.generaldonate()
# ได้ เงินได้สุทธิ หลังหักค่าใช้จ่ายและค่ารถหย่อนทั้งหมดมาคำนวณภาษีตามขั้นบันได
employee.ladder()
employee.showdata()





        
        


            

