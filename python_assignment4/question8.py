# Define a function which can generate and print
# a tuple where the values are square of numbers
# between 1 and 20 (both 1 and 20 included).


def print_tuple_square():

    lst = [i ** 2 for i in range(1, 21)]
    print(tuple(lst))

print_tuple_square()
