#Project 1

import random
x = random.randint(0,100)
y = int(input("Enter the number between 0 and 100: "))
if y >=0 and y<=100:
    True
    while x != y:
     y = int(input("Enter the next number"))

    print("Random number is",x,"and you predicted the number")
         
else:
    print("enter the valid number")
    y = int(input("Be sure to enter the number between 0 and 100: "))
    while x != y:
     y = int(input("Enter the next number"))

    print("Random number is",x,"and you predicted the number")