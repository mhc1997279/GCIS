import random
import time

def generate_sorted_data(size):
    array_1 = [random.randint(1, 100) for i in range(size)]
    for i in range(1, len(array_1)):
        n = array_1[i]
        j = i - 1
        while j >= 0 and n < array_1[j]:
            array_1[j + 1] = array_1[j]
            j-= 1
        array_1[j + 1] = n
    return array_1

def binary_search(sorted_array, target):
    left, right = 0, len(sorted_array) - 1

    while left <= right:
        mid = (left + right) // 2

        if sorted_array[mid] == target:
            return mid
        
        elif sorted_array[mid] > target:
            right = mid - 1
        
        else:
            left = mid + 1

    return None

def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left_half = merge_sort(array[:mid])
    right_half = merge_sort(array[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return None

def main():
    small_data = [34, 7, 23, 32, 5, 62, 29, 12, 40, 8]
    sorted_data = generate_sorted_data(len(small_data))
    print("Sorted Data:", sorted_data)
    sorted_array = [5, 7, 8, 12, 23, 29, 32, 34, 40, 62]
    print(binary_search(sorted_array, 29)) 
    print(binary_search(sorted_array, 100))

    large_data = [55, 22, 89, 34, 67, 90, 15, 72, 39, 44] + [random.randint(1, 100) for _ in range(990)]
    sorted_large_data = merge_sort(large_data)
    print("First 10 elements:", sorted_large_data[:10])
   
    target = 72
    start_time = time.perf_counter()
    linear_search(sorted_large_data, target)
    linear_duration = time.perf_counter() - start_time
    start_time = time.perf_counter()
    binary_search(sorted_large_data, target)
    binary_duration = time.perf_counter() - start_time
    print("Linear Search Result Time Taken:",linear_duration,"seconds")
    print("Binary Search Result Time Taken:",binary_duration,"seconds")

main()