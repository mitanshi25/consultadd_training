# 10. Write a program that asks five times to guess the lucky number. Use a while loop and a counter,
# such as
# counter=1
# While counter <= 5:
# print(“Type in the”, counter, “number”
# counter=counter+1
# The program asks for five guesses (no matter whether the correct number was guessed or not). If the
# correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”.
# After the fifth guess it stops and prints “Game over!”.
print("you have five chances to guess the lucky number between 1-100")
import random
# a = random.randint(1,101)
# guess = int(input("guess the lucky no"))
counter =1

while counter<= 5:
    a = random.randint(1,101)
    guess = int(input("guess the lucky no"))
    if (guess == a):
        print("good guess")
        counter=+1
    else:
        print("Try Again")
   

    if(counter == 5):
        print("game over")
    
    counter += 1

    
    
