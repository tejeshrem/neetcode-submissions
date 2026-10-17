class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = curr_min = 1
        res = max(nums)
        for n in nums:
            vals = (n, n * curr_max, n * curr_min)
            curr_max = max(vals)
            curr_min = min(vals)
            res = max(res, curr_max)

        return res            
            
            

        