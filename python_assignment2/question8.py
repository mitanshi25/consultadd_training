# 8. Write a program that accepts a string as an input from the user and calculate the number of digits
# and letters.
# Sample input: consul72
# Expected output: Letters 6 Digits 2

 



digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
 

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
               'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
 


string = input("enter a string")
 

total_digits = 0
total_letters = 0
 

for s in string:
 
    # if character found in all_digits then increment total_digits by one
    if s in digits:
        total_digits += 1
 
    # if character not found in all_digits then increment total_letters by one
    else:
        total_letters += 1
 
print("Total letters found :-", total_letters)
print("Total digits found :-", total_digits)