from inspect import isgenerator

def pow(x):
    return x ** 2

def some_gen(begin, end, func):

    term = begin
    for _ in range(end):
        yield term
        term = func(term)

gen = some_gen(3, 5, pow)
print('Is generator?', isgenerator(gen))
print(list(gen))
