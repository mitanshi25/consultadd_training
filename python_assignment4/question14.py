# 14. Write a program in Python to find the values which are not
# divisible by 3 but are a multiple of 7.
# Make sure to use only higher order functions
nl = []
for x in range(0, 100):
    if (x % 3 == 0) and (x % 7 == 0):
        nl.append(str(x))
print (','.join(nl))