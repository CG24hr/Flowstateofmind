#ค่าเฉลี่ยแบบประเมินสุขภาพจิตขององค์กร
number = int(input('number of people in your organization :'))
allscore =[]
count = 0
n = number
print('Rate your score regarding to these following problems.')
print('0 = Not at all , 1 = Several days , 2 = More than half the days , 3 = Nearly every day')
while count < number : 
    print('person' , count + 1)
    a = int(input('Little interest or pleasure in doing things? : '))
    b = int(input('Feeling down, depressed or hopeless? : '))
    c = int(input('Trouble falling asleep, staying asleep, or sleeping too much : '))
    d = int(input('Feeling tired or having little energy : '))
    e = int(input('Poor appetite or overeating : '))
    f = int(input('Feeling bad about yourself : '))
    g = int(input('Trouble concentrating on things : '))
    h = int(input('Moving or speaking so slowly that other people could have noticed or being so fidgety or restless : '))
    i = int(input('Thoughts that you would be better off dead or of hurting yourself in some way : '))
    if 0 <= a <= 3 and 0 <= b <= 3 and 0 <= c <= 3 and 0 <= d <= 3 and 0 <= e <= 3 and 0 <= f <= 3 and 0 <= g <= 3 and 0 <= h <= 3 and 0 <= i <= 3 : 
        count = count + 1
        individualscore = a + b + c + d + e + f + g + h + i
        allscore.append(individualscore)
    else :
        print('Please  check your answer again.')
print('All individual PHQ9 score is' , allscore)
averagescore = sum(allscore) // len(allscore)
if 0 <= averagescore <= 4 :
    print('Average organized PHQ9 mental health score is in None-minimal Depression severity')
elif 5 <= averagescore <= 9 :
    print('Average organized PHQ9 mental health score is in Mild Depression severity')
elif 10 <= averagescore <= 14 :
    print('Average organized PHQ9 mental health score is in Moderate Depression severity')
elif 15 <= averagescore <= 19 :
    print('Average organized PHQ9 mental health score is in Moderately-severe Depression severity')
elif 20 <= averagescore <= 27 :
    print('Average organized PHQ9 mental health score is in Severe Depression severity')
else :
    print('Please check your answer again.')

print('Average organized PHQ9 mental health score is' , averagescore )