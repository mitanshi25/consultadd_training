# 4. Write a program in Python using
# generators to reverse the string.
# Input String = “Consultadd Training”

def reverse(str1):
    length = len(str1)
    for i in range(length - 1, -1):
        yield str[i]
input = "Consultadd training"
for x in reverse(input):
    print(x)