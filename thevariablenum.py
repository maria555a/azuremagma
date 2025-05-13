import string
import keyword

name = input("Type variable name: ")

is_variable_name_valid = True

if not name:
    is_variable_name_valid = False
elif name in keyword.kwlist:
    is_variable_name_valid = False
elif name[0].isdigit():
    is_variable_name_valid = False
elif name.count('_') > 1:
    value = False


else:
    for sign in name:
        if sign.isupper():
            is_variable_name_valid = False
            break
        if sign in string.whitespace:
            is_variable_name_valid = False
            break
        if sign in string.punctuation and sign != '_':
            is_variable_name_valid = False
            break
print(is_variable_name_valid)



