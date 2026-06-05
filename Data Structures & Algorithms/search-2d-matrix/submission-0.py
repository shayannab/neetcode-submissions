class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix) - 1

        while top <= bot:
            mid = (top + bot) // 2
            if target > matrix[mid][-1]:
                top=mid+1
            elif target < matrix[mid][0]:
                bot=mid-1
            else:
                 break
        if top > bot:       
            return False
        row=mid
        l, r = 0, len(matrix[row]) - 1
        while l <= r:
            mid = (l + r) // 2
            if target == matrix[row][mid]:
                return True
            elif target > matrix[row][mid]:
                l=mid+1
            else:
                r=mid-1
        
        return False