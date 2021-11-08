# 11. In the previous question, insert break after the “Good guess!” print statement. break will terminate
# the while loop so that users do not have to continue guessing after they found the number. If the user
# does not guess the number at all, print “Sorry but that was not very successful”.

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
        break
    else:
        print("Sorry but that was not very successful")
   

    if(counter == 5):
        print("game over")
    
    counter += 1