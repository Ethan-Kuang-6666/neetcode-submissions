class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i in range(len(s)):
            last[s[i]] = i

        l = 0
        r = 0
        res = []
        for i in range(len(s)):
            r = max(r, last[s[i]])
            if i == r:
                res.append(r - l + 1)
                l = r + 1
                r = r + 1
        return res
