# 1. Write a program which uses map() and filter()
#  to make a list whose elements are squares of even
# numbers in [1,2,3,4,5,6,7,8,9,10].
# Hints: Use filter() to filter even elements of the given
#  listUse map() to generate a list of squares of the
# numbers in the filtered list. Use lambda() to define
#  anonymous functions.


li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
eve_num = map(lambda x: x**2, filter(lambda   x: x % 2 == 0, li))
print(eve_num)