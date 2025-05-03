lst = [0, 7, 0, 8, 0, 0, 5, 9, 6]
zeros = lst.count(0)
lst2 = [num for num in lst if num != 0] + [0] * lst.count(0)
print(lst2)

