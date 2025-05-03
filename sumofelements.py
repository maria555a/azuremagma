lst = [0, 2, 5, 7, 8, 9, 3]
if not lst:
    result = 0
else:
    numbers_sum = sum(lst[::2])
    result = numbers_sum * lst[-1]
print(result)

