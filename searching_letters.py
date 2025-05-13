import string
entered_letters = input("Enter two letters separated by a hyphen: ")
start_let, end_let = entered_letters.split('-')
all_letters = string.ascii_letters

start_index = all_letters.index(start_let)
end_index = all_letters.index(end_let)

result = all_letters[start_index:end_index + 1]
print(result)

