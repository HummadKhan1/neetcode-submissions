class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}

        for num in range(len(nums)):
            complement = target - nums[num]
            if complement in num_dict:
                return [num_dict[complement], num]
            else:
                num_dict[nums[num]] = num
        return []