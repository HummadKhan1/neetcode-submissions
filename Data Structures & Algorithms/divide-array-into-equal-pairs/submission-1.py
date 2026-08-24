class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        for cnt in count.values():
            if cnt % 2 == 1:
                return False
        return True