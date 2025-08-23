from collections import Counter

def count_occurrences(str1, str2):
    # """
    # Calculate the total number of occurrences of each unique character of str2 in str1.
    # """
    # # Create a frequency map for characters in str1
    # freq_map = Counter(str1)

    # # Get unique characters from str2
    # unique_chars = set(str2)

    # # Sum the occurrences of each unique character in str1
    # total = 0
    # for char in unique_chars:
    #     total += freq_map.get(char, 0)

    # return total
    s = set(str2)
    count = 0
    for elem in s:
        count += str1.count(elem)
    return count


# Input
str1 = input().strip()
str2 = input().strip()

# Calculate and print the result
result = count_occurrences(str1, str2)
print(result)