class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0
        maxL, maxR, L = 0, 0, 0

        for R in range(len(nums)):
            if curSum < 0:
                curSum = 0
                L = R
            curSum += nums[R]
            if maxSum < curSum:
                maxSum = curSum
                maxL, maxR = L, R
        print(maxL, maxR)
        return maxSum