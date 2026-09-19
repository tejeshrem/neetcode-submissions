class Solution:
    def floodFill(
        self,
        image: List[List[int]],
        sr: int,
        sc: int,
        color: int
    ) -> List[List[int]]:

        orig = image[sr][sc]

        if orig == color:
            return image

        ROWS, COLS = len(image), len(image[0])

        directions = [
            [1, 0],
            [0, 1],
            [-1, 0],
            [0, -1]
        ]

        def bfs(r, c):
            image[r][c] = color

            q = collections.deque()
            q.append([r, c])

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc

                    if (
                        0 <= nr < ROWS and
                        0 <= nc < COLS and
                        image[nr][nc] == orig
                    ):
                        image[nr][nc] = color
                        q.append([nr, nc])

        bfs(sr, sc)

        return image