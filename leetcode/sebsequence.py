class Solution(object):
    def isSubsequence(self, s, t):
        i, j = 0, 0  # Initialize pointers for both strings s and t
    
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1  # Move to the next character in s
            j += 1  # Always move to the next character in t
        
        # If all characters in s have been matched in t, s is a subsequence of t
        return i == len(s)