# The city provides its citizens with a Walk Generating App on their phones
#  -- everytime you press the button it sends you an array of one-letter strings
# representing directions to walk (eg. ['n', 's', 'w', 'e']).
# You always walk only a single block for each letter (direction) 
# and you know it takes you one minute to traverse one city block,
# so create a function that will return true if the walk the app gives you will
# take you exactly ten minutes (you don't want to be early or late!) and will,
# of course, return you to your starting point.
# Return false otherwise.

# (['n','s','n','s','n','s','n','s','n','s']),         True,    
# (['w','e','w','e','w','e','w','e','w','e','w','e']), False,   len(walk) == 12
# (['n','n','n','s','n','s','n','s','n','s']),         False,   count(n) != count(s) "n = 6, s = 4"

def is_valid_walk(walk):
    x = 0
    y = 0
    if len(walk) != 10:
        return False
    
    for i in walk:
        if i == 'n':
            y += 1
        if i == 's':
            y -= 1
        if i == 'w':
            x += 1
        if i == 'e':
            x -= 1
    return x == 0 and y == 0
            

print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']))
print(is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']))
print(is_valid_walk(['n','n','n','s','n','s','n','s','n','s']))
print(is_valid_walk(['s', 's', 'n', 'e', 'n', 'n', 's', 'w']))  # False len(walk) != 10