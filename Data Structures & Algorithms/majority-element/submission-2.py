from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        most_freq = max(count.values())

        return max(count, key=count.get)
        