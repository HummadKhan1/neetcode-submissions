class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        pairs = set()

        for n in nums:
            if n in pairs:
                pairs.remove(n)
            else:
                pairs.add(n)
        if pairs:
            return False
        return True        