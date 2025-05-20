def common_elements():
    multiples_3 = {i for i in range(100) if i % 3 == 0}
    multiples_5 = {i for i in range(100) if i % 5 == 0}

    return multiples_3 & multiples_5

result = common_elements()
print(result)
