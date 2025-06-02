def generate_cube_numbers(end):
    num = 2
    while True:
        cube = num ** 3
        if cube > end:
            return
        yield cube
        num += 1

print(list(generate_cube_numbers(100)))
