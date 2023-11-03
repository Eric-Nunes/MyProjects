def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid  # Target found, return its index
        elif arr[mid] < target:
            left = mid + 1  # Adjust the left boundary
        else:
            right = mid - 1  # Adjust the right boundary

    return -1  # Target not found in the list

if __name__ == "__main__":
    # Example usage:
    sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17]
    target = 7

    result = binary_search(sorted_list, target)

    if result != -1:
        print(f"Target {target} found at index {result}")
    else:
        print(f"Target {target} not found in the list")
