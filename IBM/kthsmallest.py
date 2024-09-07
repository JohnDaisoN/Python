def find_kth_missing(arr, k):
    arr.sort()  # Sort the array first
    prev = 0  # Track the previous number (starting with 0)

    for num in arr:
        missing_between = num - prev - 1  # Find how many numbers are missing between prev and num
        if missing_between >= k:
            # If the missing numbers between prev and num cover the kth missing, return the result
            return prev + k
        k -= missing_between  # Subtract the missing numbers from k
        prev = num  # Move prev to the current number

    # If k is still greater, return the result after the last element in the array
    return arr[-1] + k

# Example usage
arr = [2, 3, 7, 10]
k = 5
result = find_kth_missing(arr, k)
print(f"The {k}th missing number is: {result}")
