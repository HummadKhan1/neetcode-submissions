class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = len(nums)+1
        L = 0
        cur_sum = 0
        for R in range(len(nums)):
            cur_sum += nums[R]
            while cur_sum >= target:
                if R-L+1 < min_len:
                    min_len = R-L+1
                cur_sum -= nums[L]
                L += 1
        if min_len == len(nums)+1:
            min_len = 0
        return min_len