# 15. Write a program in Python to multiply the elements of
# a list by itself using a traditional function
# and pass the function to map() to complete the operation.


def multiply(list):
    return list * list

print(list(map(multiply, eval(input("enter a list: ")))))