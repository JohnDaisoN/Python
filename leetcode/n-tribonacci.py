class Solution(object):
    def tribonacci(self, n):
        
        
        if (n == 2):
            return 1
        elif (n == 1):
            return 1
        elif (n == 0):
            return 0
        else:
            return self.tribonacci( n-1) + self.tribonacci( n-2) + self.tribonacci( n-3)
        """
        :type n: int
        :rtype: int
        """
        