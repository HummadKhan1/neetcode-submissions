class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Sliding Window, can return index beginning and end of subarray
        L = 0
        resultL, resultR = 0, 0
        curSum = 0
        maxSum = nums[0]
        for R in range(len(nums)):
            if curSum < 0:
                curSum = 0
                L = R
            curSum += nums[R]
            if curSum > maxSum:
                maxSum = curSum
                resultL, resultR = L, R
        return maxSum