class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res = 0

        for n in nums[:]:
            if n == val:
                nums.remove(n)
            else:
                res += 1
        return res
            