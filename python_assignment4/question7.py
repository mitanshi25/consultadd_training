# 7. Define a function that can accept two strings
#  as input and print the string with the maximum length
# in the console. If two strings have the same length,
#  then the function should print both the strings line
# by line.


def max_string(s1, s2):
    # print(len(s1))
    # print(len(s2))
    if (len(s1) == len(s2)):
        print(s1, s2)
    else:
        print(len(s1))
        print(len(s2))

s1 = input("enter first string")
s2 = input("enter second string")

max_string(s1, s2)