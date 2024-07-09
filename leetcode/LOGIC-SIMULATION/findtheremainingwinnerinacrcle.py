class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        array = [elem for elem in range(1,n+1)]
        i = 0
        while array:
            # i += k
            if i + k  < len(array):
                print(array)


                lasteliminated = array.pop(i+k-1)
                print(array)
                i += 1
            else:
                print(array)
                i -= 1

                lasteliminated = array.pop((i+k)%len(array))
                print(array)
                i += 1
                



        return lasteliminated
'''
i can solve this in a free mental state
but couldnot do today

womp womp
'''

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        winner = 0  # Josephus problem is 0-indexed in calculation
        for i in range(1, n + 1):
            winner = (winner + k) % i
        return winner + 1