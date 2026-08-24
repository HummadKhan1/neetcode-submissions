class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dup_dict = {}
        for i in range(len(nums)):
            if nums[i] in dup_dict:
                if abs(i-dup_dict[nums[i]]) <= k:
                    return True
            dup_dict[nums[i]] = i
        return False