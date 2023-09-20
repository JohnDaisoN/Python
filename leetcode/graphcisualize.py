class Solution(object):
 def uniquePaths(self, m, n):
        
    dp = [[1] * n for _ in range(m)]

    # Calculate the number of unique paths for each cell
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    # The value in the bottom-right corner represents the number of unique paths
    return dp[m - 1][n - 1]