lst = []
if len(lst) == 0:
    result = [[], []]
    print(result)


lst = [9, 6, 3, 9, 8, 9, 6, 9]
part = len(lst) // 2
lst1 = lst[:part]
lst2 = lst[part:]
result = [lst1, lst2]
print(result)


lst = [3, 5, 2, 5, 7]
part = (len(lst) + 1) // 2
lst1 = lst[:part]
lst2 = lst[part:]
result = [lst1, lst2]
print(result)

