class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        maxLeft = []
        curSum = 0
        for n in nums:
            maxLeft.append(curSum)
            curSum += n
        print(maxLeft)
        maxRight = [0] * len(nums)
        curSum = 0
        for i in range(len(nums)-1,-1,-1):
            maxRight[i] = curSum
            curSum += nums[i]
        print(maxRight)
        for i in range(len(nums)):
            if maxLeft[i] == maxRight[i]:
                return i
        return -1