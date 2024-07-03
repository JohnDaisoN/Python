'''
basic solition
i implemented it - first try - only beats 31.78 % - mineis the commonest senseless approach 

but i didnt think it woul dbe this bad
i might paste a beter solution under this if i feel so

explanation in notes in july mP-5 summer bird
'''
class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        l = 0
        r = 0
        # length = 0
        while r < len(arr):
            if arr[r] % 2 == 1:
                
                r += 1
            else:
                r += 1
                l = r



            if r - l == 3:
                return True
        return False

'''
i am putting below code not because of its efficiency but due to its simplicity

inm bwlow code no need to like check for left, rigjt pointers and stuff

simple one variable needed only like count 

easy to understand
'''

class Solution(object):
    def threeConsecutiveOdds(self, arr):
        count = 0 # Initialize count to keep track of consecutive odd numbers

        for num in arr: # Iterate through each element in the array
            if num % 2 != 0: # Check if the current element is odd
                count += 1 # Increment the count if it's odd
                if count == 3: # If we have found three consecutive odds, return true
                    return True
            else: # If the element is even, reset the count to 0
                count = 0

        return False