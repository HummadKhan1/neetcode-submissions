class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = False
        decreasing = False

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                if not increasing and decreasing:
                    return False
                elif not increasing and not decreasing:
                    increasing = True
            elif nums[i] < nums[i-1]:
                if not decreasing and increasing:
                    return False
                elif not decreasing and not increasing:
                    decreasing = True
        return True