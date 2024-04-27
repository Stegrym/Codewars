# Write a function that takes in a string of one or more words,
# and returns the same string, but with all words that have five or
# more letters reversed (Just like the name of this Kata).
# Strings passed in will consist of only letters and spaces.
# Spaces will be included only when more than one word is present.

# Examples:

# "Hey fellow warriors"  --> "Hey wollef sroirraw" 
# "This is a test"       --> "This is a test" 
# "This is another test" --> "This is rehtona test"
def spin_words(sentence):
    result = []
    for i in sentence.split():
        if len(i) >=5:
            result.append(i[::-1])
        else:
            result.append(i)
    return ' '.join(result)


print(spin_words("Hey fellow warriors"))
print(spin_words("This is a test"))
print(spin_words("This is another test"))