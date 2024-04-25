# For simplicity, you'll have to capitalize each word, check out
# how contractions are expected to be in the example below.

# Input:  "How can mirrors be real if our eyes aren't real"
# Output: "How Can Mirrors Be Real If Our Eyes Aren't Real"


def to_jaden_case(string):
    return ' '.join(i.capitalize() for i in string.split(' '))


print(to_jaden_case("How can mirrors be real if our eyes aren't real"))
