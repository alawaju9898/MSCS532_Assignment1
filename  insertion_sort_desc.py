def insertion_sort_desc(arr):
  
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Shift elements that are less than key to the right
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


# Example usage
if __name__ == "__main__":
    # Example list
    numbers = [7, 2, 9, 1, 5, 3]

    print("Original list:", numbers)
    sorted_numbers = insertion_sort_desc(numbers)
    print("Sorted in descending order:", sorted_numbers)
