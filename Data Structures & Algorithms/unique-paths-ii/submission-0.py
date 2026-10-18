class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        dp = {(m-1,n-1) : 1}

        def dfs(r,c):

            if r == m or c == n or grid[r][c] == 1 :
                return 0
            elif (r,c) in dp:
                return dp[(r,c)]
            dp[(r,c)] = dfs(r+1,c)+dfs(r,c+1)
            return dfs(r,c)

        return dfs(0,0)                 
            


        