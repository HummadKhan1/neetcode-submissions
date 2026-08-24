class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_Sums = {0: 1}
        cur_sum = 0
        res = 0
        for n in nums:
            cur_sum += n
            diff = cur_sum - k
            res += prefix_Sums.get(diff, 0)
            prefix_Sums[cur_sum] = prefix_Sums.get(cur_sum, 0) + 1
        return res