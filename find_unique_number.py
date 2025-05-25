def find_unique_value(my_list):
    for value in my_list:
        if my_list.count(value) == 1:
            return value

my_list = [1, 3, 6, 7, 3, 1, 7]

unique_value= find_unique_value(my_list)
print(unique_value)
