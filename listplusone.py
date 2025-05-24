def add_one(new_list):
    number_str = ''.join(map(str, new_list))

    number = int(number_str)
    number += 1

    return [int(digit) for digit in str(number)]

result =  add_one([3, 5, 7, 8])
print(result)
