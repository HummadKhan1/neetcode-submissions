class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        L = 0
        for R in range(len(nums)):
            while L <= len(nums)-1 and nums[L] == val:
                nums.remove(nums[L])
            L += 1
        return len(nums)