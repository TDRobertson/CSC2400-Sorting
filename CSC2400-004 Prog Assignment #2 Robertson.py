# File: CSC2400-004 Prog Assignment #2 Robertson.py
# Author: Thomas D. Robertson II
# Assignment: Sorting Algorithms Analysis
# Due Date: 10/27/23
# Description: This program will implement the various sorting algorithms and measure their runtimes.

import time
import random
import copy
from datetime import datetime

# Generate an array of random numbers based on the value of k
def generate_random_numbers(k):
    """
    Generate an array of random numbers based on the value of k

    Args:
        k: The value of k to generate the array of random numbers
    :returns: An array of random numbers based on the value of k

    """
    num_numbers = 10 ** k
    return [random.randint(0, num_numbers) for _ in range(num_numbers)]

# Generate an array of increasing numbers based on the value of k
def generate_increasing_numbers(k):
    """
    Generate an array of increasing numbers based on the value of k

    Args:
        k: The value of k to generate the array of increasing numbers
    :returns: An array of increasing numbers based on the value of k

    """
    num_numbers = 10 ** k
    return list(range(1, num_numbers + 1))

# Generate an array of decreasing numbers based on the value of k
def generate_decreasing_numbers(k):
    """
    Generate an array of decreasing numbers based on the value of k

    Args:
        k: The value of k to generate the array of decreasing numbers
    :returns: An array of decreasing numbers based on the value of k

    """
    num_numbers = 10 ** k
    return list(range(num_numbers, 0, -1))

# Get the value of k from the user for a size between 0 and 12
while True:
    # try to get the value of k from the user
    try:
        # get the value of k from the user
        k = int(input("Enter the value for k (this will give a list of random, increasing, and decreasing values of 10^k size: "))
        # check to see if the value of k is between 0 and 6
        if 0 <= k <= 6:
            break
        # if the value of k is not between 0 and 6, print an error message and try again
        else:
            print("Invalid value for k. It must be between 0 and 6. Try again.")
    # if the value of k is not an integer, print an error message and try again
    except ValueError:
        print("Please enter a valid integer.")


# generate an array of random numbers
random_array = generate_random_numbers(k)

# generate an array of increasing numbers
increasing_array = generate_increasing_numbers(k)

# generate an array of decreasing numbers
decreasing_array = generate_decreasing_numbers(k)

# REQUIRED Shell sort implementation method
def shell_sort(array):
    """
    Shell sort implementation method

    Args:
        array: The array to be sorted
    :returns: The sorted array

    """
    # Start with a big gap, then reduce the gap
    n = len(array)
    gap = n // 2

    # Do a gapped insertion sort for this gap size.
    while gap > 0:
        for i in range(gap, n):
            temp = array[i]
            j = i

            # Shift earlier gap-sorted elements up until the correct location for a[i] is found
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap

            array[j] = temp

        gap //= 2

    return array

# REQUIRED Insertion sort implementation method
def insertion_sort(array):
    """
    Insertion sort implementation method
    Args:
        array: The array to be sorted
    :returns: The sorted array

    """
    # Traverse from starting index to the end of the array
    for i in range(1, len(array)):
        temp = array[i]
        j = i

        # Move elements of array[0..i-1], that are greater than temp, to one position ahead of their current position
        while j > 0 and array[j - 1] > temp:
            array[j] = array[j - 1]
            j -= 1

        array[j] = temp

    return array

# REQUIRED selection sort implementation method
def selection_sort(array):
    """
    Selection sort implementation method
    Args:
        array: The array to be sorted
    :returns: The sorted array

    """
    # Traverse through all array elements
    for i in range(len(array)):
        min_index = i

        # Find the minimum element in remaining unsorted array
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        array[i], array[min_index] = array[min_index], array[i]

    return array

# REQUIRED bubble sort implementation method
def bubble_sort(array):
    """
    Bubble sort implementation method
    Args:
        array: The array to be sorted
    :return: The sorted array

    """
    # Traverse through all array elements
    n = len(array)
    for i in range(n):
        # Last i elements are already in place
        swapped = False
        # Traverse the array from 0 to n-i-1
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                # Set swapped to True so that next pass can be performed if there is a swap
                swapped = True
        # If no two elements were swapped, the list is already sorted
        if not swapped:
            break
    return array

# Extra sorting methods for comparison start here

# Helper functions for sorting methods, merge sort, and heap sort
# heapify method for heap sort
def heapify(array, n, i):
    """
    heapify method for heap sort
    Args:
        array: The array to be sorted
        n: The size of the array
        i: The index of the current node
    :return: The sorted array

    """
    # Find largest among root, left child and right child
    largest = i
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is greater than root
    if l < n and array[l] > array[largest]:
        largest = l

    # See if right child of root exists and is greater than the largest so far
    if r < n and array[r] > array[largest]:
        largest = r

    # Change root, if needed
    if largest != i:
        array[i], array[largest] = array[largest], array[i]  # swap

        # Heapify the root.
        heapify(array, n, largest)

# quick sort partition helper function
def partition(array, low, high):
    """
    quick sort partition helper function
    Args:
        array: The array to be sorted
        low: Starting index
        high: Ending index
    :return: The sorted array

    """
    # pivot (Element to be placed at right position)
    pivot = array[high]
    # Index of smaller element and indicates the right position of pivot found so far
    i = low - 1
    for j in range(low, high):
        # If current element is smaller than the pivot
        if array[j] <= pivot:
            i += 1
            # swap array[i] and array[j]
            array[i], array[j] = array[j], array[i]
    # swap array[i+1] and array[high] (or pivot)
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

# quick sort non-recursive implementation method
def iterative_quick_sort(array):
    """
    quick sort non-recursive implementation method
    Args:
        array: The array to be sorted
    :return: The sorted array

    """
    n = len(array)
    # Create an auxiliary stack
    stack = []

    # initialize top of stack
    stack.append(0)
    # initialize end of stack
    stack.append(n - 1)

    # Keep popping from stack while it is not empty
    while stack:
        high = stack.pop()
        low = stack.pop()

        # Set pivot element at its correct position in sorted array
        pivot_idx = partition(array, low, high)

        # If there are elements on left side of pivot, then push left side to stack
        if pivot_idx - 1 > low:
            stack.append(low)
            stack.append(pivot_idx - 1)

        # If there are elements on right side of pivot, then push right side to stack
        if pivot_idx + 1 < high:
            stack.append(pivot_idx + 1)
            stack.append(high)

    return array


# merge sort helper function
def merge(left, right):
    """
    merge sort helper function
    Args:
        left: The left array to be sorted
        right: The right array to be sorted
    :return: The sorted array

    """
    merged = []
    i, j = 0, 0

    # Traverse both arrays simultaneously
    while i < len(left) and j < len(right):
        # Pick the smaller element and add it to the merged array
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        # If right element is smaller, add it to the merged array
        else:
            merged.append(right[j])
            j += 1

    # Add any remaining elements from the left array
    while i < len(left):
        merged.append(left[i])
        i += 1

    # Add any remaining elements from the right array
    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged

# merge sort non-recursive implementation method
def iterative_merge_sort(array):
    """
    merge sort non-recursive implementation method
    Args:
        array: The array to be sorted
    :return: The sorted array

    """
    n = len(array)
    width = 1

    # Merge subarrays in bottom up manner
    while width < n:
        # Pick starting point of different subarrays of current size
        for i in range(0, n, 2 * width):
            # Merge subarrays of current size
            left = array[i:i + width]
            # If right array is not empty
            right = array[i + width:i + 2 * width]
            # Merge the left and right arrays
            array[i:i + 2 * width] = merge(left, right)
        # Increasing subarray size by power of 2
        width *= 2

    return array

# heap sort implementation method
def heap_sort(array):
    """
    heap sort implementation method
    Args:
        array: The array to be sorted
    :return: The sorted array

    """
    n = len(array)

    # Build a maxheap
    for i in range(n, -1, -1):
        # Heapify root node
        heapify(array, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        # Swap elements
        array[i], array[0] = array[0], array[i]
        # Heapify root element
        heapify(array, i, 0)

    return array

# Counting sort implementation method
def counting_sort(array, exp):
    """
    Counting sort implementation method
    Args:
        array: The array to be sorted
        exp: The exponent to be used
    :return: The sorted array
    """
    n = len(array)
    output = [0] * n
    count = [0] * 10  # As we're considering numbers, we have 10 possible digits (0 to 9)

    # Store count of occurrences in count[]
    for i in range(n):
        index = (array[i] // exp) % 10
        count[index] += 1

    # Change count[i] so that count[i] contains actual position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = (array[i] // exp) % 10
        output[count[index] - 1] = array[i]
        count[index] -= 1
        i -= 1

    # Copy the output array to the original array
    for i in range(n):
        array[i] = output[i]


# radix sort implementation method
def radix_sort(array):
    """
    radix sort implementation method
    Args:
        array: The array to be sorted
    :return: The sorted array

    """
    # Get maximum element
    max_num = max(array)
    exp = 1

    # Sort elements based on place value
    while max_num // exp > 0:
        counting_sort(array, exp)
        exp *= 10

    return array

# bucket sort implementation method
def bucket_sort(array):
    """
    bucket sort implementation method
    Args:
        array: The array to be sorted
    :return: The sorted array

    """
    # Step 1: Find the maximum and minimum values in the list
    max_value = max(array)
    min_value = min(array)

    # Step 2: Create buckets
    bucket_count = len(array)
    bucket_range = (max_value - min_value) / bucket_count
    buckets = [[] for _ in range(bucket_count)]

    # Step 3: Insert elements into their respective buckets
    for num in array:
        bucket_index = int((num - min_value) / bucket_range)
        bucket_index = min(bucket_index, bucket_count - 1)  # Ensure the bucket_index is within bounds
        buckets[bucket_index].append(num)

    # Step 4: Sort individual buckets and merge
    sorted_arr = []
    for bucket in buckets:
        # Using built-in sort for individual buckets
        bucket.sort()
        sorted_arr.extend(bucket)

    return sorted_arr

# Extra sorting methods for comparison end here

# open the output file to collect results
output_file = open("sorting_results.txt", "a")

# print the date and time the run started to the output file
output_file.write("\nRun started at: " + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "\n\n")

# time the sorting functions and print the results to the output file and console
def time_sorting_function(sort_function, sort_name, k):
    """
    time the sorting functions and print the results to the output file and console
    Args:
        sort_function: The sorting function to be timed
        sort_name: The name of the sorting function
        k: The value of k to generate the array of random, increasing, and decreasing numbers
    :return: None

    """
    print(f"Time taken to sort list of random, increasing, and decreasing numbers using {sort_name} for 10^{k} numbers:")
    print(f"Time taken to sort list of random, increasing, and decreasing numbers using {sort_name} for 10^{k} numbers:", file=output_file)

    # make copies of the lists to be sorted
    random_list_copy = copy.deepcopy(random_array)
    increasing_list_copy = copy.deepcopy(increasing_array)
    decreasing_list_copy = copy.deepcopy(decreasing_array)

    # time the sorting functions for the random list and print list to text file and console
    start_time = time.time()
    sort_function(random_list_copy)
    end_time = time.time()
    print(f"Time taken to sort random numbers: {end_time - start_time:.6f} seconds")
    print(f"Time taken to sort random numbers: {end_time - start_time:.6f} seconds", file=output_file)

    # time the sorting functions for the increasing list and print list to text file and console
    start_time = time.time()
    sort_function(increasing_list_copy)
    end_time = time.time()
    print(f"Time taken to sort increasing numbers: {end_time - start_time:.6f} seconds")
    print(f"Time taken to sort increasing numbers: {end_time - start_time:.6f} seconds", file=output_file)

    # time the sorting functions for the decreasing list and print list to text file and console
    start_time = time.time()
    sort_function(decreasing_list_copy)
    end_time = time.time()
    print(f"Time taken to sort decreasing numbers: {end_time - start_time:.6f} seconds")
    print(f"Time taken to sort decreasing numbers: {end_time - start_time:.6f} seconds", file=output_file)
    print()
    print(file=output_file)

# Call the time_sorting_function for each sorting function five times each
# List of sorting functions and their names
sort_functions = [
    (shell_sort, "Shell Sort"),
    (insertion_sort, "Insertion Sort"),
    (selection_sort, "Selection Sort"),
    (bubble_sort, "Bubble Sort"),
    (iterative_quick_sort, "Iterative Quick Sort"),
    (iterative_merge_sort, "Iterative Merge Sort"),
    (heap_sort, "Heap Sort"),
    (radix_sort, "Radix Sort"),
    (bucket_sort, "Bucket Sort"),
]

# Time and print results for each sorting function
for sort_function, sort_name in sort_functions:
    # Run the time_sorting_function 5 times
    for i in range(5):
        print(f"\nRun {i + 1} for {sort_name}:")
        print(f"\nRun {i + 1} for {sort_name}:", file=output_file)
        time_sorting_function(sort_function, sort_name, k)
        print("-" * 50)
        print("-" * 50, file=output_file)

# print the date and time the run ended to the output file
output_file.write("\nRun ended at: " + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "\n")

# close the output file
output_file.close()

# print a message to the user that the results have been saved to the output file
print(f"Results have been saved to {output_file.name}.")
