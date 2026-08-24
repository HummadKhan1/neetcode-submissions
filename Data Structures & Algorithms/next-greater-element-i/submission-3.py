class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Idx = {n:i for i, n in enumerate(nums1)}
        res = [-1] * len(nums1)
        stack = []

        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                val = stack.pop()
                idx = nums1Idx[val]
                res[idx] = nums2[i]
            if nums2[i] in nums1Idx:
                stack.append(nums2[i])
        return res