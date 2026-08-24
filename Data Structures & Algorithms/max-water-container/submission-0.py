class Solution:
    def maxArea(self, heights: List[int]) -> int:
        R = len(heights)-1
        L = 0
        max_area = 0

        while(R >= L):
            min_height = min(heights[L], heights[R])
            cur_area = (R-L)*min_height
            max_area = max(max_area, cur_area)
            if heights[L]>= heights[R]:
                R -= 1
            else:
                L+=1
        return max_area