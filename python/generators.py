def sequence_generator(sequence):
    for item in sequence:
        yield item


for number in sequence_generator([1, 2, 3, 4]):
    print("number:", number)

# generator expression
generator = (item for item in [1, 2, 3, 4])
for number in generator:
    print("number via generator:", number)


def fibonacci_generator(stop=10):
    curr_fib, next_fib = 0, 1
    for _ in range(stop):
        fib = curr_fib
        curr_fib, next_fib = next_fib, curr_fib + next_fib

        yield fib


for number in fibonacci_generator(15):
    print("fib num:", number)