class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        L = 0
        cur = 0
        increasing = False
        res = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                if increasing:
                    cur += nums[i]
                else:
                    cur = nums[i] + nums[i-1]
                    increasing = True
            else:
                increasing = False
            res = max(res, cur)
        return res
            