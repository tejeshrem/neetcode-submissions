class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        t,b = 0, m-1

        while t <= b:
            row = (t+b)//2
            if target > matrix[row][-1]:
                t = row + 1
            elif target < matrix[row][0]:
                b = row - 1
            else:
                break

        row = (t+b)//2
        l, r = 0, n-1

        while l <= r:
            m = (l+r)//2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False
        


