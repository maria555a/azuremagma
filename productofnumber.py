num = int(input("Enter a number: "))

if num <= 9:
    print(num)
else:
    while num > 9:
        result = 1
        for digit in str(num):
            result *= int(digit)
        num = result
    print(num)
