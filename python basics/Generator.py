# Generator using yield
def topten():
    # This is not possible with return
    yield 1
    yield 2
    yield 3

value = topten()

print(value.__next__())
# or
print(next(value))
print(next(value))