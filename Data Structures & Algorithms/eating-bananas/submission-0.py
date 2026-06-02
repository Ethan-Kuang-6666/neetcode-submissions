class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r

        while l <= r:
            mid = (l + r) // 2
            t = 0
            for i in range(len(piles)):
                t += math.ceil(piles[i] / mid)
            if t <= h:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return res


        