# Greedy Algorithm using Selection Sort

def selection_sort(arr):

    n = len(arr)

    for i in range(n):

        # Assume current index has minimum value
        min_index = i

        # Find actual minimum element
        for j in range(i + 1, n):

            if arr[j] < arr[min_index]:
                min_index = j

        # Swap elements
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

# Main Program
numbers = [64, 25, 12, 22, 11]

print("Original Array:")
print(numbers)

sorted_array = selection_sort(numbers)

print("Sorted Array:")
print(sorted_array)