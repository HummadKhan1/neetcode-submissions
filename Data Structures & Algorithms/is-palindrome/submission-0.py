class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_arr = []
        for c in s:
            if c.isalnum():
                new_arr.append(c.lower())
        L = 0
        R = len(new_arr)-1
        while L < R:
            if new_arr[L] != new_arr[R]:
                return False
            L += 1
            R -= 1
        return True
            
            