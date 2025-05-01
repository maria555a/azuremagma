while True:
    num_one = float(input("Enter number: "))
    operation = input("Choose operation (+, -, *, /): ")

    if operation not in {'+', '-', '*', '/'}:
        print("Wrong value")
        continue

    num_two = float(input("Enter number: "))
    result = None

    if operation == "+":
        result = num_one + num_two
    elif operation == "-":
        result = num_one - num_two
    elif operation == "*":
        result = num_one * num_two
    elif operation == "/":
        if num_two == 0:
            print("Invalid value: division by zero!")
            continue
        result = num_one / num_two

    if result is not None:
        print(f"Result: {result}")

    while True:
        request = input("Do you want to continue? (yes/no): ").strip().lower()
        if request == 'yes':
            break

        elif request == 'no':
            print('End')
            exit()
        else:
            print('Invalid request')

