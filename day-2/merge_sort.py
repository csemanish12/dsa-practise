class MergeSort:
    def merge(self, numbers, low, middle, high):
        left = low
        right = middle + 1
        temp = []

        while left <= middle and right <= high:
            if numbers[left] <= numbers[right]:
                temp.append(numbers[left])
                left += 1
            else:
                temp.append(numbers[right])
                right += 1
        while left <= middle:
            temp.append(numbers[left])
            left += 1

        while right <= high:
            temp.append(numbers[right])
            right += 1

        for i in range(low, high + 1):
            numbers[i] = temp[i - low]

        pass

    def merge_sort(self, numbers, left, right):
        if left < right:
            middle = (left + (right - 1)) // 2
            self.merge_sort(numbers, left, middle)
            self.merge_sort(numbers, middle + 1, right)
            self.merge(numbers, left, middle, right)


merge_sort = MergeSort()
input_1 = [2, 1, 5, 4, 6, 7, 9, 3]
merge_sort.merge_sort(input_1, 0, len(input_1)-1)
print("after sort:", input_1)
