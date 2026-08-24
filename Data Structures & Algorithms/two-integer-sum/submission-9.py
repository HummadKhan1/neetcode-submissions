class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        parameters: arr nums, int target.
        return: indices.
        Really asking: Two sum problem.
        Constraints: i != j.
        variables: nums_dict,  
        '''
        nums_dict = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nums_dict:
                return [nums_dict[complement], i]
            nums_dict[nums[i]] = i
        