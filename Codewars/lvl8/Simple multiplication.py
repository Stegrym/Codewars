# This kata is about multiplying a given number by eight
# if it is an even number, and by nine otherwise.


def simple_multiplication(number):
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9


print(simple_multiplication(2))   # 2 even number     --> 2  * 8 = 16
print(simple_multiplication(5))   # 5 not even number --> 5  * 9 = 45
print(simple_multiplication(10))  # 10 even number    --> 10 * 8 = 80
