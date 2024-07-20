'''
You are given two arrays rowSum and colSum of non-negative integers where rowSum[i] is the sum of the elements in the ith row and colSum[j] is the sum of the elements of the jth column of a 2D matrix. In other words, you do not know the elements of the matrix, but you do know the sums of each row and column.

Find any matrix of non-negative integers of size rowSum.length x colSum.length that satisfies the rowSum and colSum requirements.

Return a 2D array representing any matrix that fulfills the requirements. It's guaranteed that at least one matrix that fulfills the requirements exists.

 

Example 1:

Input: rowSum = [3,8], colSum = [4,7]
Output: [[3,0],
         [1,7]]
Explanation: 
0th row: 3 + 0 = 3 == rowSum[0]
1st row: 1 + 7 = 8 == rowSum[1]
0th column: 3 + 1 = 4 == colSum[0]
1st column: 0 + 7 = 7 == colSum[1]
The row and column sums match, and all matrix elements are non-negative.
Another possible matrix is: [[1,2],
                             [3,5]
'''

#explanation in mp-5 greenbird book ;)
class Solution(object):
    def restoreMatrix(self, rowSum, colSum):
        """
        :type rowSum: List[int]
        :type colSum: List[int]
        :rtype: List[List[int]]
        """
        ROWS,COLS = len(rowSum), len(colSum)

        res = [[0]*COLS for _ in range(ROWS)]

        for r in range(len(res)):
            res[r][0] = rowSum[r]

        for c in range(COLS):
            cur_col_sum = 0
            for r in range(ROWS):
                cur_col_sum += res[r][c]

            r =0
            while cur_col_sum > colSum[c]:
                diff = cur_col_sum - colSum[c]
                max_shift = min(res[r][c],diff)
                res[r][c] -= max_shift
                res[r][c+1] += max_shift
                cur_col_sum -= max_shift
                r += 1

        return res

        

        