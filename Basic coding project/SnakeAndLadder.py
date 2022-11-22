# สร้าง class เป็น boardgame 
# โดยผู้เล่นแต่ละคนในเกมเป็น object มี Attribute คือชื่อและตำแหน่ง , Method ได้แก่ walk, snake, ladder
# snake
    # ช่อง 35 ไป 6
    # ช่อง 61 ไป 43
    # ช่อง 89 ไป 46
    # ช่อง 97 ไป 60
# ladder
    # ช่อง 8 ไป 32
    # ช่อง 17 ไป 23
    # ช่อง 39 ไป 58
    # ช่อง 44 ไป 76
    # ช่อง 65 ไป 86

class SnakeAndLadder :
    def __init__(self, name) :
        self.name = name
        print('Welcome', self.name)

    def walk(self, player, position, dice) :
        self.player = player
        self.position = position
        self.dice = dice
        self.position = self.position + self.dice
        
    def snake(self, player) :
        self.player = player
        self.runaway = self.position
        if self.position == 35 :
            self.runaway = 6
            print('Run away from snake.')
        elif self.position == 61 :
            self.runaway = 43
            print('Run away from snake.')
        elif self.position == 89 :
            self.runaway = 46
            print('Run away from snake.')
        elif self.position == 97 :
            self.runaway = 60
            print('Run away from snake.')
        else :
            self.runaway = self.runaway

        return self.runaway
    
    def ladder(self, player) :
        self.player = player
        self.climb = self.runaway
        if self.runaway == 8 :
            self.climb = 32 
            print('You find a ladder, Climb it !')
        elif self.runaway == 17 :
            self.climb = 23
            print('You find a ladder, Climb it !')
        elif self.runaway == 39 :
            self.climb = 58
            print('You find a ladder, Climb it !')
        elif self.runaway == 44 :
            self.climb = 76
            print('You find a ladder, Climb it !')
        elif self.runaway == 65 :
            self.climb = 86
            print('You find a ladder, Climb it !')
        else :
            self.climb = self.climb
        
        print(self.player , 'is standing on', self.climb)
        self.End = input('Would you like to end your turn ? <Press Enter to continue.>')
        return self.climb



#เรียกใช้ Class
Name1 = input('Enter your name :')
Name2 = input('Enter your name :')
player1 = SnakeAndLadder(Name1)
player2 = SnakeAndLadder(Name2)

player1P = 0
player2P = 0

Start = input('Are you ready ? <Press Enter to start your journey.>')
import random

while player1P < 99 and player2P < 99 :
    dice1 = random.randint(1, 6)
    player1.walk(Name1, player1P, dice1)
    player1.snake(Name1)
    position1 = player1.ladder(Name1)
    player1P = position1
    
    dice2 = random.randint(1, 6)
    player2.walk(Name2, player2P, dice2)
    player2.snake(Name2)
    position2 = player2.ladder(Name2)
    player2P = position2

if player1P > player2P :
    print('The winner is', Name1)
elif player2P > player1P :
    print('The winner is', Name2)



 

 