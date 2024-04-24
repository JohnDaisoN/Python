class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_index = {}  # A dictionary to store the index of each character
        max_length = 0  # Initialize the maximum length of the substring
        start = 0  # Initialize the start index of the current substring

        for end in range(len(s)):
            if s[end] in char_index and char_index[s[end]] >= start:
            # If the character is already in the current substring
            # Update the start index to the next character
                start = char_index[s[end]] + 1
            char_index[s[end]] = end  # Update the index of the character
            max_length = max(max_length, end - start + 1)  # Update the maximum 

        return max_length
        