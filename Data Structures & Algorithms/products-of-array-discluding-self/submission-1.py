class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftSide = 1
        leftArr = [1]
        for i in range(1,len(nums)):
            leftSide *= nums[i-1]
            leftArr.append(leftSide)
        print(leftArr)
        rightSide = 1
        rightArr = [1] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            rightSide *= nums[i+1]
            rightArr[i] = rightSide
        print(rightArr)
        new_list = []
        for i in range(len(leftArr)):
            new_list.append(leftArr[i]*rightArr[i])
        return new_list