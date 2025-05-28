def difference(*nums):
    if not nums:
        return 0
    diff = max(nums) - min(nums)

    return round(diff, 2)

print(difference(2, 5, 15))
print(difference(6, -12))
print(difference(4.6, 7.8))
print(difference())
