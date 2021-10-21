# 2. Write a program in Python to perform the following operator based task:
# Ask user to choose the following option first:
# If User Enter 1 - Addition
# If User Enter 2 - Subtraction
# If User Enter 3 - Division
# If User Enter 4 - Multiplication
# If User Enter 5 - Average
# Ask user to enter two numbers and keep those numbers in variables num1 and num2
# respectively for the first 4 options mentioned above.
# Ask the user to enter two more numbers as first and second for calculating the average as
# soon as the user chooses an option 5.
# At the end if the answer of any operation is Negative print a statement saying “NEGATIVE”
# NOTE: At a time a user can only perform one action.

print("please choose from one of these operations ")
print("1- Addition \n2- Subtraction \n3- Division \n4- Multiplication \n5-Average")
choice = int(input("please select from 1-5"))
num1 =int(input("enetr a no"))
num2 =int(input("enetr a no"))

if(choice == 1):
    print(num1+num2)
elif(choice == 2):
    a =0
    a = num1-num2
    if(a<0):
        print("Negative")
    else:
        print(a)
elif(choice == 3):
    print(num1/num2)
elif(choice == 4):
    print(num1*num2)
elif(choice == 5):
    print((num1+num2)/2)
else:
    print("negative number")

# num1=int(input("enter a number"))
# num2=int(input("enter a number"))
# print("enter the option")
# a=int(input("enter a number from 1 to 5:"))
# res=0
# if a=='1':
#     res=num1+num2
#     print(res)
# elif a=='2':
#     res=num1-num2
#     print(res)
# elif a=='3':
#     res=num1/num2
#     print(res)
# elif a=='4':
#     res= num1*num2
#     print(res)
# elif a=='5':
#     res= num1+num2/2
#     print(res)
# else:
#     print("input is negative")
# print(num1 ,a, num2,":",res)
    
