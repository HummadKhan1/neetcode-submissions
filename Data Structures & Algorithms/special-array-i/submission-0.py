class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        '''
        Really asking: two pointer solution. L, R compare the two targets and see if there is at least 1 even and 1 odd.
        '''
        L = 0

        for i in range(1, len(nums)):
            if nums[i-1] % 2 == 0 and nums[i] % 2 == 0:
                return False
            elif nums[i-1] % 2 == 1 and nums[i] % 2 == 1:
                return False
        return True