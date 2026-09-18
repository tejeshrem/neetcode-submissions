class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        prev = {}

        for i, n in enumerate(nums):
            if n in prev and i - prev[n] <= k:
                return True
            prev[n] = i

        return False


        