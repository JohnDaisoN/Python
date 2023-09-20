class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0  # Initialize a count for planted flowers
        i = 0  # Initialize an index to iterate through the flowerbed
        while i < len(flowerbed):
            if flowerbed[i] == 0:
                # Check if the current spot and its neighbors are empty (0)
                if i == 0 or flowerbed[i - 1] == 0:
                    if i == len(flowerbed) - 1 or flowerbed[i + 1] == 0:
                        flowerbed[i] = 1  # Plant a flower
                        count += 1  # Increment the count
            i += 1

        # Check if you were able to plant at least n flowers
        return count >= n