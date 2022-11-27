#สร้าง class หรือเทียบเท่ากับแม่พิมพ์
class Robot() :
    
    class Hand () :
        #class variable หรือตัวแปรที่มี life cycle นอกเหนือจากใน method
        type = 'Hand accessory'
        L = 'left side'
        R = 'right side'
        #  สร้าง method (หรือเทียบเท่า function) , keyword self เป็นค่าคงที่ใช้ มีค่าเท่ากับตัว object ที่เรียกใช้งานมันอยู่ 
        def stabilizehand(self) : 
            #กำหนด Attribute หรือ คุณสมบัติ / instance variable
            self.flex = 'Flex MCP 90 degree.'
            self.extend = 'Extend wrist 30 degree'
            print('Safe position of hand = {} and {}'.format(self.flex, self.extend))
        def movehandvertically(self, flex, extend) :
            self.flex = flex
            self.extend = extend
            print('Flex hand {}'.format(self.flex), 'degree')
            print('Extend hand {}'.format(self.extend), 'degree')
        def movehandhorizontally(self, adduct, abduct) :
            self.adduct = adduct
            self.abduct = abduct
            print('Adduct hand {}'.format(self.adduct), 'degree')
            print('Abduct hand {}'.format(self.abduct), 'degree')



#สร้าง object หรือวัตถุ ( ประกอบด้วย attribute , method )
hand1 = Robot.Hand()
print('Your accessory is', hand1.L , hand1.type)
hand1.stabilizehand() 

flex = int(input('Degree of wrist flextion :'))
extend = int(input('Degree of wrist extension :'))
hand1.movehandvertically(flex, extend)

adduct = int(input('Degree of wrist adduction : '))
abduct = int(input('Degree of wrist abduction :'))
hand1.movehandhorizontally(adduct, abduct)

