class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.HouseRobber(nums[:-1]), self.HouseRobber(nums[1:]))
    
    def HouseRobber(self, nums):

        rob1, rob2 = 0,0
        for num in nums:
            temp = max(rob1+num, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2


        