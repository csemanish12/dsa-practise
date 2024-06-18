def sequence_generator(sequence):
    for item in sequence:
        yield item


for number in sequence_generator([1, 2, 3, 4]):
    print("number:", number)

# generator expression
generator = (item for item in [1, 2, 3, 4])
for number in generator:
    print("number via generator:", number)
