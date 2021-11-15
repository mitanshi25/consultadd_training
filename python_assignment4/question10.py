# 10. Write a program which uses filter() to make a
# list whose elements are even numbers between 1
# and 20 (both included)
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
eve_num = map(lambda x: x**2, filter(lambda   x: x % 2 == 0, li))
print(eve_num)