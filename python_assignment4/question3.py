# reate a function that takes a list and returns a new list with unique elements of the first list.


def unique (lst):
    a =[]
    for i in lst:
        if i not in a:
            a.append(i)
    return a


lst = unique([1,2,3,3,3,4,4,5])
print(lst)

