class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = 1
        for R in range(len(nums)):
            while L <= len(nums)-1 and nums[L] == nums[R]:
                nums.remove(nums[L])
            L += 1
        return len(nums)