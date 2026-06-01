class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        top = 0
        bot = n - 1

        while top <= bot:
            mid = top + (bot - top) // 2
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] < target:
                top = mid + 1
            else:
                bot = mid - 1

        row = bot

        l = 0
        r = m - 1
        while l <= r:
            mid = l + (r - l) // 2
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False