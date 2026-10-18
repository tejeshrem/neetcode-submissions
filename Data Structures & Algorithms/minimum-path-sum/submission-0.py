class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for j in range(n + 1):
            dp[m][j] = float('inf')

        for i in range(m + 1):
            dp[i][n] = float('inf')
        
        dp[m-1][n] = 0

        for r in range(m-1,-1,-1):
            for c in range(n-1,-1,-1):
                dp[r][c] = grid[r][c] + min(dp[r+1][c], dp[r][c+1])
        
        print(dp)
        return dp[0][0]

        