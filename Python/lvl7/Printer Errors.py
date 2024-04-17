# Examples:

# not_error_letter = 'ABCDEFGHIJKLM'
# error_letter = 'NOPQRSTUVWXYZ'

# string ="aaabbbbhaijjjm"
# printer_error(string) => "0/14"

# string="aaaxbbbbyyhwawiwjjjwwm"
# printer_error(string) => "8/22"


def printer_error(s: str):
    not_error = 'ABCDEFGHIJKLM'
    string = len(s)
    errors = 0
    for i in s:
        if i.upper() not in not_error:
            errors += 1
    return f'{errors}/{string}'


string = "aaabbbbhaijjjm"
print(printer_error(string))  # => "0/14"

string = "aaaxbbbbyyhwawiwjjjwwm"
print(printer_error(string))  # => "8/22"
