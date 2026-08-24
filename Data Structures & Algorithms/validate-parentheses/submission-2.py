class Solution:
    def isValid(self, s: str) -> bool:
        prnt_dict = {'}': '{', ']': '[', ')': '('}
        stack = []
        for c in s:
            if c in prnt_dict.values():
                stack.append(c)
            elif not stack or prnt_dict[c] != stack.pop():
                return False
        if stack:
            return False
        return True