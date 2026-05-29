class Solution:
    def checkValidString(self, s: str) -> bool:
        lmin = 0
        lmax = 0

        for i in range(len(s)):
            if s[i] == "(":
                lmin += 1
                lmax += 1
            elif s[i] == ")":
                lmin -= 1
                lmax -= 1
            else:
                lmin -= 1
                lmax += 1

            if lmin < 0:
                lmin = 0
            if lmax < 0:
                return False

        return lmin == 0