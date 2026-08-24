class Solution:
    def isPalindrome(self, s: str) -> bool:
        R = len(s) - 1
        L = 0
        while L < R:
            if s[L].isalnum() == False:
                L += 1
                continue
            elif s[R].isalnum() == False:
                R -= 1
                continue
            if s[L].lower() != s[R].lower():
                return False
            L += 1
            R -= 1
        return True
            
            