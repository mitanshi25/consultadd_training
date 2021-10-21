import random
randnumber = random.randint(1,100)
userguess =None
guesses = 0

while(userguess !=randnumber):

    userguess =int(input("enter your guess"))
    guesses +=1
    if userguess == randnumber:
        print("you guessed it right")
    else: 
        if(userguess >randnumber):
            print("you need to guess a lower no")
        else:
            print("you need to guess a upper no")