#  Write a function that accepts a string and 
# prints the number of uppercase letters and lowercase
# letters.
# Sample input: “abcSdefPghijQkl”
# Expected Output: No. of Uppercase characters :
#  3 No. of Lower case Characters : 12

def upper_lower(s):
    upper =0
    lower =0
    
    for j in s:
        if j.isupper():
            upper += 1
        elif j.islower():
            lower += 1
        else:
            pass
    return (upper , lower)

s = "abcSdefPghijQkl"
print(upper_lower(s))


























        

