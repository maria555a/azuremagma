import string
import keyword

name = input("Type variable name: ")

value = True

if not name:
    value = False
elif name in keyword.kwlist:
    value = False
elif name[0].isdigit():
    value = False
elif name.count('_') > 1:
    value = False


else:
    for sign in name:
        if sign.isupper():
            value = False
            break
        if sign in string.whitespace:
            value = False
            break
        if sign in string.punctuation and sign != '_':
            value = False
            break
print(value)



