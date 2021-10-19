# 2. Create a variable of type complex and
# swap it with another variable of type integer.

a = 1 + 2j
b = 11
print("the value of a before swapping is:", a)
print("the value of b before swapping is:", b)
a, b = b, a
print("the value of a:", a, "\nand the value of b after swapping:", b)

