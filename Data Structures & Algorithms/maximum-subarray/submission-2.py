class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        current = 0
        
        for num in nums:
            if current < 0:
                current = 0

            current += num
            res = max(res, current)

        return res

        


        