class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = {}
        res = 0
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        for cnt in count.values():
            res += (cnt * (cnt-1))//2
        
        return res