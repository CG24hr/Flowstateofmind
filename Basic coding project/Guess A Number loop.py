import random
print("Guessing game")
print("Choose 1 to 100")
print("My guess is correct(C), higher(H), or lower(L)")

a = 1
b = 100

#เดาตัวเลขที่คอมสุ่ม
ChoosingNumber = int(input("Choose one number : "))
g = random.randint(a,b)
while ChoosingNumber != g :
    if ChoosingNumber > g :
        print("Your number is higher.")
        ChoosingNumber = int(input("Choose one number : "))
    if ChoosingNumber < g :
        print("Your number is lower.")
        ChoosingNumber = int(input("Choose one number : "))
if ChoosingNumber == g :
    print("Your number is correct.")


#ให้คอมสุ่มเรื่อยๆว่าเราเดาตรงไหม
print("Let's Computer guess.")
a = 1
b = 100
ChoosingNumber = int(input("Choose one number : "))
while b > a :
    g = random.randint(a,b)
    #คอมตอบ
    print("My guess is" , g)
    #เราตอบ (ว่า Correct(C), Higher(H), or lower(L))
    answer = input("Your guess is : ")
    if answer == "H" :
        b = g - 1
        print("I will try again.")
    elif answer == "L" :
        a = g + 1
        print("I will try again.")
    elif answer == "C" :
        a = g 
        b = g
        print("Good job.")
    else :
        print("INVALID.")
print("It must be" , g)