class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        parameters: int arrays: nums1, nums2.
        return: arr.
        Really asking: two pointer problem.
        Constraints:
        Variables: i pointer, j pointer, res.
        '''
        nums1Idx = { n:i for i, n in enumerate(nums1)}
        res = [-1] * len(nums1)
        stack = []

        for j in range(len(nums2)):
            while stack and stack[-1] < nums2[j]:
                val = stack.pop()
                idx = nums1Idx[val]
                res[idx] = nums2[j]
            if nums2[j] in nums1Idx:
                stack.append(nums2[j])
        return res
