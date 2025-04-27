num = int(input("Enter a 4-digit number: "))
thousands = num // 1000
hundreds = (num % 1000) // 100
tens = (num % 100) // 10
ones = num % 10

print(thousands)
print(hundreds)
print(tens)
print(ones)


