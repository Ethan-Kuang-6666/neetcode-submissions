class Solution:
    def checkValidString(self, s: str) -> bool:
        l_count = 0
        s_count = 0

        for i in range(len(s)):
            if s[i] == "(":
                l_count += 1
            elif s[i] == "*":
                s_count += 1
            else:
                if l_count > 0:
                    l_count -= 1
                elif s_count > 0:
                    s_count -= 1
                else:
                    return False

        if l_count > s_count:
            return False
            
        r_count = 0
        s_count = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ")":
                r_count += 1
            elif s[i] == "*":
                s_count += 1
            else:
                if r_count > 0:
                    r_count -= 1
                elif s_count > 0:
                    s_count -= 1
                else:
                    return False
        
        return True