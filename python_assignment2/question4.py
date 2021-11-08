# 4.Write a program in Python to break and continue if the following
# cases occurs:
# If user enters a negative number just break the loop and print “It’s Over”
# If user enters a positive number just continue in the loop and print
# “Good Going”
while True:
    n = int(input("enter a number: "))
    if n < 0:
        print("it's Over.")
        break
    else:
        print("Good Going.")
        continue

    

