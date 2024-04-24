class Solution(object):
    def find132pattern(self, nums):
        n = len(nums)
        if n < 3:
            return False

        # Initialize a stack to keep track of potential '2' candidates
        stack = []

        # Initialize the '3' candidate as negative infinity
        third = float('-inf')

        # Traverse the array from right to left
        for j in range(n - 1, -1, -1):
            # If we find a number smaller than the '3' candidate, return True
            if nums[j] < third:
                return True

            # While the current number is greater than the top of the stack, update the '3' candidate
            while stack and nums[j] > stack[-1]:
                third = stack.pop()

            # Push the current number onto the stack as a potential '2' candidate
            stack.append(nums[j])

        return False

'''
here an super way to use stack
here last element check to ultimately find '3' sub
'2' is popped 
'2' is compared with next element to find 1
but next element greater than '3'(stack[-1]) then it becomes the new '3'
current '3' becomes '2' and used to consequently compare with next elements
'''
