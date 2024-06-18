class SequenceIterator:
    def __init__(self, sequence):
        self._sequence = sequence
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._sequence):
            item = self._sequence[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration


for item in SequenceIterator([1, 2, 3, 4, 5]):
    print(item)


# python for loop internals
sequence = SequenceIterator([1, 2, 3, 4])
iterator = sequence.__iter__()
while True:
    try:
        item = iterator.__next__()
    except StopIteration:
        break
    else:
        print("item from for loop mimic:", item)
