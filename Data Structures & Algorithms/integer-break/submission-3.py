class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1

        for curr in range(1,n+1):
            for i in range(1, curr):
                diff = curr - i 
                dp[curr] = max(dp[curr], dp[diff] * i, i * diff)
        print(dp)
        return dp[n]

                
                