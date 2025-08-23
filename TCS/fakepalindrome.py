from collections import Counter
string = input()


def is_palindrome(s):
    # ones = 0
    
    # for elem in Counter(s).values():
    #     print(Counter(s),f'this is the counter for stirng {s}')
    #     if elem == 1:
    #         ones += 1
    #     elif elem != 2:
    #         return False
    # if ones == 0 or ones == 1:
    #     print(True)
    #     return True
    count = {}
    for elem in s:
        if elem not in count:
            count[elem] = 1
        else:
            count[elem] -= 1
    count = {k:v for k,v in count.items() if v>0}
        
    print(count,f'this is the counter for {s}')
    if not count:
        return True

    if len(count.keys()) == 1:
        
        if 1 in count.values():
            return True
        
    return False

count = 0
for i in range(len(string)):
    for j in range(i,len(string)):
        if is_palindrome(string[i:j+1]):
            count += 1
print(count)


# above code passed 6/7


from collections import Counter

def is_fake_palindrome(s):
    """
    Check if the string can be rearranged into a palindrome.
    """
    freq = Counter(s)
    odd_counts = sum(1 for count in freq.values() if count % 2 != 0)
    return odd_counts <= 1

def count_fake_palindromic_substrings(A):
    """
    Count the number of fake palindromic substrings in the string A.
    """
    n = len(A)
    count = 0

    for i in range(n):
        freq = {}
        odd_counts = 0
        for j in range(i, n):
            char = A[j]
            freq[char] = freq.get(char, 0) + 1

            # Update the number of characters with odd counts
            if freq[char] % 2 == 1:
                odd_counts += 1
            else:
                odd_counts -= 1

            # If at most one character has an odd count, it's a fake palindrome
            if odd_counts <= 1:
                count += 1

    return count

# Input
string = input().strip()

# Count fake palindromic substrings
result = count_fake_palindromic_substrings(string)

# Output
print(result)

