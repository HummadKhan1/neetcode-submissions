class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_list = []

        for num in nums:
            if num not in nums_list:
                nums_list.append(num)
            else:
                return True
        return False