class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict = {}
        for i in range(len(nums)):
            sum_dict[nums[i]] = i
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in sum_dict:
                if i != sum_dict[complement]:
                    return [i, sum_dict[complement]]