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
    
    
