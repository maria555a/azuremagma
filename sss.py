num = int(input("Enter a 5-digit number: "))
ten_thousands = num // 10000
thousands = (num % 10000) // 1000
hundreds = (num % 1000) // 100
tens = (num % 100) // 10
ones = num % 10

print(ones, tens, hundreds, thousands, ten_thousands)
