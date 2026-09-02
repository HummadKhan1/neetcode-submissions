from collections import Counter
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        count = Counter(nums)

        a = max(count.keys())
        count[a] -= 1
        if count[a] == 0:
            del count[a]
        
        b = max(count.keys())
        
        c = min(count.keys())
        count[c] -= 1
        if count[c] == 0:
            del count[c]
        
        d = min(count.keys())

        return (a * b) - (c * d)
