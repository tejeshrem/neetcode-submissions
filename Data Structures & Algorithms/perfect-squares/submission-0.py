class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n+1)
        dp[0] = 0

        for curr in range(1,n+1):
            for s in range(1, curr+1):
                square = s*s
                if square > curr:
                    break
                dp[curr] = min(dp[curr], 1+dp[curr-square])

        return dp[n]



        