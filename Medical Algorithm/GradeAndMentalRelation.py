
class studentclass() :

    def grade (self, N) :
        self.N = N
        count = 0
        examscore = []
        while count < N :
            count = count + 1
            print('Student No.', count)
            correct = int(input('Correct point :'))
            midterm = int(input('Midterm score :'))
            final = int(input('Final score :'))
            total = correct + midterm + final

            if 0 <= correct <= 30 and 0 <= midterm <= 30 and 0 <= final <= 40 :
                if 80 <= total <= 100 :
                    print('Total score is', total)
                    print('grade A') 
                elif 75 <= total <= 79 :
                    print('Total score is', total)
                    print('grade B+')
                elif 70 <= total <= 74 :
                    print('Total score is', total)
                    print('grade B')
                elif 65 <= total <= 69 :
                    print('Total score is', total)
                    print('grade C+')
                elif 60 <= total <= 64 :
                    print('grade C')
                elif 55 <= total <= 59 :
                    print('Total score is', total)
                    print('grade D+')
                elif 50 <= total <= 54 :
                    print('Total score is', total)
                    print('grade D')
                elif 0 <= total <= 49 :
                    print('Total score is', total)
                    print('grade F')
                else :
                    print('Please check your information.')
            else :
                print('Please check your information.')

            examscore.append(total)

        print('All score of students in this classroom is', examscore)
        print('Average score in this classroom is', sum(examscore)/len(examscore))
        return examscore 


    def DASS21stress (self, N) :
        self.N = N
        count = 0 
        stressscore = [] 
        print('Rate your score regarding to these following problems.')
        print('0 = Not at all , 1 = Sometimes , 2 = Often , 3 = Usually')
        while count < N :
            print('Student No.', count + 1)
            s1 = int(input('I found it hard to wind down :'))
            s2 = int(input('I tended to over-react to situations :'))
            s3 = int(input('I felt that I was using a lot of nervous energy :'))
            s4 = int(input('I found myself getting agitated :'))
            s5 = int(input('I found it difficult to relax :'))
            s6 = int(input('I was intolerant of anything that kept me from getting on with what I was doing :'))
            s7 = int(input('I felt that I was rather touchy :'))
            
            s = s1 + s2 + s3 + s4 + s5 + s6 + s7
            stressscore.append(s)
            count = count + 1 
        print('DASS21 Stress score of students in this classroom is', stressscore)
        return stressscore
    
        
        
  
    def DASS21anxiety (self, N) :
        self.N = N
        count = 0 
        anxietyscore = []
        print('Rate your score regarding to these following problems.')
        print('0 = Not at all , 1 = Sometimes , 2 = Often , 3 = Usually')
        while count < N :
            print('Student No.', count + 1)
            a1 = int(input('I was aware of dryness of my mouth :'))
            a2 = int(input('I experienced breathing difficulty (e.g. excessively rapid breathing, breathlessness in the absence of physical exertion) : '))
            a3 = int(input('I experienced trembling (e.g. in the hands) : '))
            a4 = int(input('I was worried about situations in which I might panic and make a fool of myself :'))
            a5 = int(input('I felt I was close to panic :'))
            a6 = int(input('I was aware of the action of my heart in the absence of physical exertion (e.g. sense of heart rate increase, heart missing a beat) :'))
            a7 = int(input('I felt scared without any good reason :'))
        
            a = a1 + a2 + a3 + a4 + a5 + a6 + a7         
            anxietyscore.append(a)
            count = count + 1 
        print('DASS21 anxiety score of students in this classroom is', anxietyscore)
        return anxietyscore


    def DASS21depression (self, N) :
        self.N = N
        count = 0 
        depressionscore = []
        print('Rate your score regarding to these following problems.')
        print('0 = Not at all , 1 = Sometimes , 2 = Often , 3 = Usually')
        while count < N :
            print('Student No.', count + 1)
            d1 = int(input('I could not seem to experience any positive feeling at all :'))
            d2 = int(input('I found it difficult to work up the initiative to do things :'))
            d3 = int(input('I felt that I had nothing to look forward to :'))
            d4 = int(input('I felt down-hearted and blue :'))
            d5 = int(input('I was unable to become enthusiastic about anything :'))
            d6 = int(input('I felt I was not worth much as a person :'))
            d7 = int(input('I felt that life was meaningless :'))
            
            d = d1 + d2 + d3 + d4 + d5 + d6 + d7
            depressionscore.append(d)
            count = count + 1 
   
        print('DASS21 depression score of students in this classroom is', depressionscore)
        return depressionscore
    
      


N = int(input('Number of students in classroom :'))
studentscore = studentclass()


 #หาความสัมพันธ์ระหว่างผลการเรียนและคะแนนสุขภาพจิต
import matplotlib.pyplot as plt
plt.xlabel('examination score')
plt.ylabel('DASS21 stress score')
x = studentscore.grade(N)
plt.scatter(x , studentscore.DASS21stress(N))  
plt.show()


plt.xlabel('examination score')
plt.ylabel('DASS21 anxiety score')
plt.scatter(x , studentscore.DASS21anxiety(N))  
plt.show()


plt.xlabel('examination score')
plt.ylabel('DASS21 depression score')
plt.scatter(x , studentscore.DASS21depression(N))  
plt.show()


     
           


