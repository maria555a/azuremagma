num_one = float(input("Enter number: "))
num_two = float(input("Enter number: "))
operation = input("Choose operation (+, -, *, /): ")
result = None

if operation == "+":
    result = num_one + num_two
elif operation == "-":
    result = num_one - num_two
elif operation == "*":
    result = num_one * num_two
elif operation == "/":
    if num_two == 0:
        print("Wrong value!")
    else:
        result = num_one / num_two


if result is not None:
    print(f"Result: {result}")


