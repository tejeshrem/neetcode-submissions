class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:

        mapping = defaultdict(list)
        
        for i, w in enumerate(wordsDict):
            mapping[w].append(i)
        print(mapping)
            
        res = float("inf")
        for w1 in mapping[word1]:
            for w2 in mapping[word2]:
                res = min(res, abs(w2-w1))
        
        return res

