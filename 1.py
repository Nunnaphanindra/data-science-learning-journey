
#1.Given x = 10 and y = 5, write a Python program to determine if x is greater than y.
#If x is greater than y, check if it’s also greater than 15 and print appropriate messages accordingly.

'''x=10
y=5
if x>y and x>15:
    print("x is greater than y")
    
else:
    print("x is smaller than y")'''


#Write a Python program to determine if a given number num is even or odd.
#If it’s even, check if it’s greater than 10 and print appropriate messages.

'''num=int(input("enter a number:"))
if num%2==0:
    print("even")
    if num>10:
        print("num is greater than 10")
else:
    print("odd")'''

#Write a Python program to check if a person is eligible for a credit card based on their age and income.
#•	If the person is underage, print "You are underage."
#•	If they are of age but have an income below $30,000, print "Your income is too low for a credit card."

'''age = 25
income = 28000

if age < 18:
    print("You are underage.")
elif income < 30000:
    print("Your income is too low for a credit card.")
else:
    print("You are eligible for a credit card.")'''

age=25
income=28000
if age<18:
    print("you are underage")
elif income<30000:
    print("your income is too low")
else:
    print("you are eligible")




