class BinarySearch:
    def search(self, numbers: list, target: int) -> bool:
        n = len(numbers)
        if n == 1:
            return numbers[0] == target

        start = 0
        end = len(numbers) - 1
        mid = (start + end) // 2
        found = False
        while start <= end:
            if numbers[mid] > target:
                end = mid - 1
            elif numbers[mid] < target:
                start = mid + 1
            else:
                found = True
                break
            mid = (start + end) // 2

        return found


binary_search = BinarySearch()
input_1 = [1, 2, 5, 7, 9, 10]
target_1 = 7
print("target found:", binary_search.search(input_1, target_1))

input_2 = [1, 2, 5, 7, 9, 10]
target_2 = 4
print("target found:", binary_search.search(input_2, target_2))
