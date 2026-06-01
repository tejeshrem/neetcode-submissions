class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # use a set to keep track of all seen nums
        noted = set()

        # iterate through the list
        for num in nums:
            if num in noted:
                return True
            noted.add(num)
        
        #return false if we found no dupes
        return False

        '''
        time - O(N) b/c we iterate through n nums in the list 
        space - O(N) b/c we add at most n nums 
        '''











       