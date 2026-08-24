from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        word = "balon"
        res = float('inf')
        for s in word:
            if s == 'l' or s == 'o':
                res = min(res, count[s]//2)
            else:
                res = min(res, count[s])
        if res == float('inf'):
            res = 0
        return res