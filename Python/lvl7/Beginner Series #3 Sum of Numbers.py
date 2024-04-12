# Given two integers a and b, which can be positive or negative,
# find the sum of all the integers between and including them and return it.
# If the two numbers are equal return a or b.

# (1, -2) --> 7 (1 + 0 - 1 - 2 = -2)
# (5, 2) --> 3 (5 + 4 + 3 + 2  = 14)
# (1, 1) --> 1 (1)

def get_sum(a,b):
    if a < b:
        return sum(range(a, b+1))
    elif a > b:
        return -1 *(sum(range(a*-1,b*-1+1)))
    else:
        return a


print(get_sum(1, -2))
print(get_sum(5, 2))
print(get_sum(1, 1))