# Write a function that accepts an integer n and a string s as parameters,
# and returns a string of s repeated exactly n times.

# 6, "I"     -> "IIIIII"
# 5, "Hello" -> "HelloHelloHelloHelloHello"


def repeat_str(repeat, string):
    return repeat * string


print(repeat_str(6, 'I'))
print(repeat_str(5, 'Hello'))