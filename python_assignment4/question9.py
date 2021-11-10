# . Write a function called showNumbers that takes a parameter called limit. It should print all the
# numbers between 0 and limit with a label to identify the even and odd numbers.

def shownumber(limit):

    for i in range(0, limit):
        if i==0:
            print(i,end=" ")
            print("EVEN")

        elif i%2==0:
            print(i,end=" ")
            print("EVEN")

        else:
            print(i,end=" ")

            print("ODD")

print(shownumber(4))