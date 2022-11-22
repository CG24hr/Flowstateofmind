class gun :
    #สร้าง constructor เพื่อกำหนดค่าให้ attribute
    def __init__(self, name, bullets) :
        self.name = name
        self.bullets = bullets
        print('Your starter gun is {} , {} bullets'.format(self.name,self.bullets))
    #สร้าง method : Fire , Reload
    def Fire(self, shots) :
        self.shots = shots
        self.remain = self.bullets - self.shots 
        print('Fire {} shots, Your remaining ammunitions are {}.'.format(self.shots,self.remain))
        return self.remain
    def Reload(self, fill) :
        self.fill = fill
        print('Reload', fill, 'bullets to your magazine.')
  




name = input('Select your gun :')
if name == 'AK' :
    bullets = 12
elif name == 'Shortgun' :
    bullets = 7
elif name == 'M16' :
    bullets = 20

startgun = gun(name,bullets)

shots = int(input('How many left click :'))
startgun.Fire(shots)

R = input('Would you like to reload your magazine? <Press R button>:')
fill = shots
if R == 'R' :
    startgun.Reload(fill)
else :
    None 