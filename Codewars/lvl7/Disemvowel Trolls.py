# Trolls are attacking your comment section!
# A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
# Your task is to write a function that takes a string and return a new string with all vowels removed.
# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

# Note: for this kata, [y] isn't considered a vowel.

# "This website is for losers LOL!" --> "Ths wbst s fr lsrs LL!"
# "What are you, a communist?" --> "Wht r y,  cmmnst?"


def disemvowel(text):
    letters = 'aeiouAEIOU'
    for i in letters:
        text = text.replace(i, '')
    return text


print(disemvowel("This website is for losers LOL!"))
print(disemvowel("What are you, a communist?"))