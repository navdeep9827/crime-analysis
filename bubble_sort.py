class SortingAlgorithms:
    @staticmethod
    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        return arr

    @staticmethod
    def merge_sort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2  # Find the middle of the array
            left_half = arr[:mid]  # Divide the array into two halves
            right_half = arr[mid:]

            SortingAlgorithms.merge_sort(left_half)
            SortingAlgorithms.merge_sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1

        return arr


# Example usage:
arr_bubble = [64, 34, 25, 12, 22, 11, 90]
arr_merge = [64, 34, 25, 12, 22, 11, 90]

sorted_arr_bubble = SortingAlgorithms.bubble_sort(arr_bubble.copy())
sorted_arr_merge = SortingAlgorithms.merge_sort(arr_merge.copy())

print("Bubble Sorted array:", sorted_arr_bubble)
print("Merge Sorted array:", sorted_arr_merge)
