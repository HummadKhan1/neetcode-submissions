class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        unique_elements = set(nums)
        cur_len = 0
        max_len = float("-inf")
        cur_value = 0
        for u in unique_elements:
            cur_value = u
            if u-1 not in unique_elements:
                while cur_value in unique_elements:
                    cur_len += 1
                    cur_value += 1
                max_len = max(max_len, cur_len)
            cur_len = 0
        return max_len
                    
