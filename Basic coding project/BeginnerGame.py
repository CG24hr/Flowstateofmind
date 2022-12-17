class game() :
    
    # Rock/Paper/Scissors VS. computer
    def RPS (self, Name) :
        print('Welcome', Name)
        userwin = 0
        computerwin = 0
        while True :
            options = ['rock', 'paper', 'scissor']
            user_input = input('You pick <Type Rock/Paper/Scissor> or <Q to quit> :')
            # .lower() คือทำให้ค่า string นั้นๆกลายเป็นตัวพิมพ์เล็ก เพื่อป้องกัน กรณีผู้ตอบพิมพ์ตัวพิมพ์ใหญ่มาแล้วระบบตรวจให้ผิด , .upper() ก็ตรงข้ามกัน
            if user_input.lower() == 'q' :
                print('quit')
                break
            elif user_input.lower() not in options :
                print('Play again.')
                continue 
            elif user_input.lower() in options :
                import random   
                computer = options[random.randint(0,2)]
                print('Computer pick :', computer)
                if user_input.lower() == computer :
                    print('draw') 
                elif user_input.lower() == 'rock' and computer == 'scissor' :
                    print(Name, 'win')
                    userwin = userwin + 1
                elif user_input.lower() == 'paper' and computer == 'rock' :
                    print(Name, 'win')
                    userwin = userwin + 1
                elif user_input.lower() == 'scissor' and computer == 'paper' :
                    print(Name, 'win')
                    userwin = userwin + 1
                else :
                    print('You lost!')
                    computerwin = computerwin + 1
        print(Name, 'win', userwin)
        print('Computer', 'win', computerwin)


    
    def NumberGuessing (self,name) :
        print('Welcome', name)
        import random 
        a = int(input('Type a range of number :')) 
        r = random.randrange(1,a)
        flag = False
        while flag == False :
            guess = int(input('Guess a number :'))
            if guess > r or guess < r :
                print('You got it wrong !')
                if guess > r :
                    print('Your answer is above the number.')
                elif guess < r :
                    print('Your answer is below the number.')
            elif guess == r :
                print('You got it !')
                flag = True 

               
    def Quiz (self,Name) :
        print('Welcome', Name)
        play = input('Do you want to start? <Yes/No> :')
        # lower คือทำให้ค่า string นั้นๆกลายเป็นตัวพิมพ์เล็ก
        if play.lower() != 'yes' :
            quit()
        elif play.lower() == 'yes' :
            print('Start !')
            score = 0
            answer = input(' What does CPU stand for ? :')
            if answer.lower() == 'central processing unit'  :
                print('Correct !')
                score = score + 1 
            else :
                print('Incorrect !')
            answer = input(' What does GPU stand for ? :')
            if answer.lower() == 'graphics processing unit'  :
                print('Correct !')
                score = score + 1 
            else :
                print('Incorrect !')
            answer = input(' What does RAM stand for ? :')
            if answer.lower() == 'random access memory'  :
                print('Correct !')
                score = score + 1 
            else :
                print('Incorrect !')
            answer = input(' What does PSU stand for ? :')
            if answer.lower() == 'power supply unit'  :
                print('Correct !')
                score = score + 1 
            else :
                print('Incorrect !')
        print('You got '+str(score)+'/4')
            

            



Name = input('Enter your name :')

play = game()
play.RPS(Name)
play.NumberGuessing(Name)
play.Quiz(Name)
