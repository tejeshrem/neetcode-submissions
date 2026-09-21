class Solution:
    def floodFill(self, grid: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        orig = grid[sr][sc]

        if grid[sr][sc] == color:
            return grid

        ROWS = len(grid)
        COLS = len(grid[0])

        def bfs(r,c):
            grid[r][c] = color
            q = collections.deque()
            q.append([r,c])
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc
                    if (0 <= nr < ROWS 
                        and 0 <= nc < COLS 
                        and grid[nr][nc] == orig
                    ):
                        grid[nr][nc] = color
                        q.append([nr,nc])
                        print(nr)
                        print(nc)
                        print(grid)
        
        bfs(sr,sc)

        return grid
                
                


            
        