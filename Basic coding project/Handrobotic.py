#สร้าง class หรือเทียบเท่ากับแม่พิมพ์
class HandRobot() :
    

    #สร้าง method (หรือเทียบเท่า function) , keyword self เป็นค่าคงที่ ที่ทำให้ตัว method รู้ว่ามี object ไหนเรียกใช้งานมันอยู่ 
    def stabilizehand(self) : 
        #กำหนด Attribute หรือ คุณสมบัติ
        self.flex = 'Flex MCP 90 degree.'
        self.extend = 'Extend wrist 30 degree'
        print('Safe position of hand = {} and {}'.format(self.flex, self.extend))
    def movehandvertically(self, flex, extend) :
        self.flex = flex
        self.extend = extend
        print('Flex hand{}'.format(self.flex), 'degree')
        print('Extend hand{}'.format(self.extend), 'degree')
    def movehandhorizontally(self, adduct, abduct) :
        self.adduct = adduct
        self.abduct = abduct
        print('Adduct hand', adduct, 'degree')
        print('Abduct hand', abduct, 'degree')



#สร้าง object หรือวัตถุ ( ประกอบด้วย attribute , method )
hand = HandRobot()
hand.stabilizehand() 

flex = int(input('Degree of wrist flextion :'))
extend = int(input('Degree of wrist extension :'))
hand.movehandvertically(flex, extend)

adduct = int(input('Degree of wrist adduction : '))
abduct = int(input('Degree of wrist abduction :'))
hand.movehandhorizontally(adduct, abduct)

