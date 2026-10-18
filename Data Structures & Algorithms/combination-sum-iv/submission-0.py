class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {0: 1}
        
        for curr in range(1, target + 1):
            dp[curr] = 0
            for num in nums:
                if curr - num in dp:
                    dp[curr] += dp[curr - num]
                    
        return dp[target]