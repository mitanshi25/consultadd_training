# 3. Swap two numbers using a third variable
# and do the same task without using any third variable.

a, b = 5, 6
print("value of a and b before swapping", a, b)
temp = a
a = b
b = temp
print("value of a and b after swapping", a, b)

# swapping without third variable

a, b = 5, 6
print("value of a and b before swapping", a, b)
a, b = b, a
print("value of a and b after swapping", a, b)






