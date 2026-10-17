class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        prev = {0:0}
        for c in coins:
            prev[c] = 1
        coins.sort()
        
        for curr in range(amount+1):
            if curr in prev:
                continue
            prev[curr] = 10001
            for c in coins:
                diff = curr -c
                if diff in prev:
                    numcoins = prev[diff] + 1
                    prev[curr] = min(numcoins, prev[curr])
        
        if prev[amount] != 10001:
            return prev[amount]
        else:
            return -1

                    
            


                

        