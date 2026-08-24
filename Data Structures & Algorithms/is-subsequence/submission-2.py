
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_list = list(s)
        t_list = list(t)
        L = 0
        for i in range(len(t)):
            if L > len(s)-1:
                    return True
            if s_list[L] == t_list[i]:
                L += 1
                if L > len(s)-1:
                    return True
        return False
        