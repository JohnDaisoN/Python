from itertools import combinations

def count_triplets_divisible_by_d(arr, d):
    count = 0

    # Iterate over all distinct triplets (i, j, k)
    for i, j, k in combinations(range(len(arr)), 3):
        # Check if the sum of a[i], a[j], a[k] is divisible by d
        if (arr[i] + arr[j] + arr[k]) % d == 0:
            count += 1
    
    return count

# Example usage
arr = [3, 3, 4, 7]
d = 5
result = count_triplets_divisible_by_d(arr, d)
print(f"Number of triplets divisible by {d}: {result}")
