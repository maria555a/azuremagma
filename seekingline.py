def second_index(main_str, substring):
    first = main_str.find(substring)
    if first == -1:
        return None
    second = main_str.find(substring, first + 1)
    if second == -1:
        return None
    return second

main_str = input("Enter string: " )
search_str = input("Enter substring: ")
result = second_index(main_str, search_str)
print(result)
