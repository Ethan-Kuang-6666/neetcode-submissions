class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        leftMost = [-1] * n
        rightMost = [n] * n

        stack = []

        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                leftMost[i] = stack[-1]
            stack.append(i)
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                rightMost[i] = stack[-1]
            stack.append(i)
        
        res = 0
        for i in range(n):
            left = leftMost[i] + 1
            right = rightMost[i] - 1
            res = max(res, heights[i] * (right - left + 1))

        return res