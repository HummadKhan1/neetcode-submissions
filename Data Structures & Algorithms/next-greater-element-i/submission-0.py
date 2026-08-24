class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        parameters: int arrays: nums1, nums2.
        return: arr.
        Really asking: two pointer problem.
        Constraints:
        Variables: i pointer, j pointer, res.
        '''
        res = []
        for i in range(len(nums1)):
            greaterVal = -1
            found = False
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    found = True
                elif found == True and nums2[j] > nums1[i]:
                    greaterVal = nums2[j]
                    break
            res.append(greaterVal)
        return res
