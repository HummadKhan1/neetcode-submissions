from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        unique = set(nums)
        most_freq = max(count.values())

        for u in unique:
            if count[u] == most_freq:
                return u
        