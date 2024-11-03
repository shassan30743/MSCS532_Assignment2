import time
import random

# Quick Sort implementation
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# Merge Sort implementation
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Compare the performance
def compare_algorithms():
    sizes = [1000, 5000, 10000]
    for size in sizes:
        # Create datasets
        sorted_data = list(range(size))
        reverse_sorted_data = sorted_data[::-1]
        random_data = [random.randint(0, size) for _ in range(size)]
        
        datasets = {'sorted': sorted_data, 'reverse_sorted': reverse_sorted_data, 'random': random_data}
        
        for key, data in datasets.items():
            start = time.time()
            quick_sort(data.copy())
            quick_sort_time = time.time() - start
            
            start = time.time()
            merge_sort(data.copy())
            merge_sort_time = time.time() - start
            
            print(f"Dataset: {key}, Size: {size}")
            print(f"Quick Sort Time: {quick_sort_time:.6f} seconds")
            print(f"Merge Sort Time: {merge_sort_time:.6f} seconds\n")

if __name__ == "__main__":
    compare_algorithms()
