from collections import Counter
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        a = b = 0
        c = d = float("inf")

        for n in nums:
            if n > b:
                if n > a:
                    a, b = n, a
                else:
                    b = n
            if n < d:
                if n < c:
                    c, d = n, c
                else:
                    d = n
        return (a * b) - (c * d)
