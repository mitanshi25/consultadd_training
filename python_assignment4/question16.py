'''16. What is the output of the following codes:
(i) def foo():
try:
return 1
finally:
return 2
k = foo()
print(k)

(ii) def a():
try:
f(x, 4)
finally:
print('after f')
print('after f?')
a()'''


# in case 1 the output is 2
# f is not defined in case 2