class Solution(object):
    def reverseVowels(self, s):
        # Create a set of lowercase vowels
        vowels = set(['a', 'e', 'i', 'o', 'u'])

        # Initialize pointers for the start and end of the string
        start, end = 0, len(s) - 1

        # Convert the string to a list of characters for easy manipulation
        s_list = list(s)

        while start < end:
            # Find the next vowel from the start
            while start < end and s_list[start].lower() not in vowels:
                start += 1

            # Find the next vowel from the end
            while start < end and s_list[end].lower() not in vowels:
                end -= 1

            # Swap the vowels
            s_list[start], s_list[end] = s_list[end], s_list[start]

            # Move the pointers
            start += 1
            end -= 1

        # Convert the list back to a string
        result = ''.join(s_list)

        return result
        