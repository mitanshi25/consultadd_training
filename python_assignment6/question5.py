# 5. Write an example on decorators

def inc(x):
    return x+1
def dec(x):
    return x-1
def decorator(func,x):
    result=func(x)
    return result