class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        current = nums[0]

        for i in range(1, len(nums)):
            if current + nums[i] < 0:
                res = max(res, current + nums[i], nums[i])
                current = 0
            else:
                current += nums[i]
                res = max(res, current)

        return res

        


        