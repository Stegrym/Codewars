# Define a method/function that removes from a given array of integers
# all the values contained in a second array.
# Examples (input -> output):

# [1, 1, 2, 3, 1, 2, 3, 4], [1, 3] -> [2, 2, 4]
# [1, 1, 2, 3, 1, 2, 3, 4, 4, 3, 5, 6, 7, 2, 8], [1, 3, 4, 2] -> [5, 6, 7, 8]

def remove_(integer_list, values_list):
    for i in integer_list[0:]:
        if i in values_list:
            integer_list.remove(i)
    return integer_list


print(remove_([1, 1, 2, 3, 1, 2, 3, 4], [1, 3]))
print(remove_([1, 1, 2, 3, 1, 2, 3, 4, 4, 3, 5, 6, 7, 2, 8], [1, 3, 4, 2]))
