class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Sliding Window, can return index beginning and end of subarray
        maxSum = nums[0]
        curSum = 0
        LResult, Rresult = 0, 0
        L = 0

        for R in range(len(nums)):
            if curSum < 0:
                curSum = 0
                L = R
            
            curSum += nums[R]

            if curSum > maxSum:
                maxSum = curSum
                Lresult, Rresult = L, R
        return maxSum