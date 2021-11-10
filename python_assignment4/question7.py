def max_string (s1 ,s2):
    # print(len(s1))
    # print(len(s2))
    if (len(s1) == len(s2)):
        print(s1, s2)
    else:
        print(len(s1))
        print(len(s2))

s1 = input("enter first string")
s2 = input("enter second string")

max_string(s1, s2)