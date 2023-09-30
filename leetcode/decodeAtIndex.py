class Solution(object):
 def decodeAtIndex(self, s, k):
    '''tape = ""
    repeat = 0

    for char in s:
        if char.isalpha():
            tape += char
        elif char.isdigit():
            repeat = repeat * int(char) + (int(char) - 1)

        if len(tape) >= k:
            return tape[k - 1]

    return tape'''
    
    size = 0
    
    # Calculate the size of the decoded string
    for char in s:
        if char.isdigit():
            size *= int(char)
        else:
            size += 1
    
    # Traverse the string in reverse to find the kth letter
    for char in reversed(s):
        k %= size  # Reduce k to fit within the current size
        
        if k == 0 and char.isalpha():
            return char
        
        if char.isdigit():
            size //= int(char)
        else:
            size -= 1
