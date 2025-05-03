lst = []
if len(lst) == 0:
    result = [[], []]
    print(result)


lst = [9, 6, 3, 9, 8, 9, 6, 9]
mid = len(lst) // 2
lst1 = lst[:mid]
lst2 = lst[mid:]
result = [lst1, lst2]
print(result)


lst = [3, 5, 2, 5, 7]
mid = (len(lst) + 1) // 2
lst1 = lst[:mid]
lst2 = lst[mid:]
result = [lst1, lst2]
print(result)

