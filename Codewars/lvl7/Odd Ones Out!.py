# Challenge: You are given a list of numbers.
# The numbers each repeat a certain number of times.
# Remove all numbers that repeat an odd number of times while keeping everything else the same.

# odd_ones_out([1, 2, 3, 1, 3, 3]) = [1, 1]
# In the above example:

# the number 1 appears twice
# the number 2 appears once
# the number 3 appears three times
# 2 and 3 both appear an odd number of times, so they are removed from the list.
#  The final result is: [1,1]


def odd_ones_out(numbers):
    result = []
    for i in numbers:
        if numbers.count(i) % 2 == 0:
            result.append(i)
    return result
    # return [i for i in numbers if numbers.count(i) % 2 == 0]


print(odd_ones_out([1, 2, 3, 1, 3, 3]))
