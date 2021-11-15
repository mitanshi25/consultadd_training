# 13. Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce().
import functools
delim  =""
reduce_num = functools.reduce(lambda x, y: str(x) + delim + str(y), list(range(1,8)))
print(reduce_num)