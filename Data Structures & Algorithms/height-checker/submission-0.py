class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        '''
        parameter: int arr heights:: current order of students.
        return: NUMBER OF indices where heights[i] != expected[i].
        Really asking: create expected[i] arr. keep track of res which is the number of different heights.
        '''
        expected = sorted(heights)
        res = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                res += 1
        return res
