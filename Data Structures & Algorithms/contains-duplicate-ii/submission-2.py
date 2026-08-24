class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dup_set = set()
        L=0
        for R in range(len(nums)):
            if R-L > k:
                dup_set.remove(nums[L])
                L += 1
            if nums[R] in dup_set:
                return True
            dup_set.add(nums[R])
        return False