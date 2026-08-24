class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        max_left_arr = [0]*n
        max_right_arr = [0]*n
        max_left_arr[0] = height[0]
        max_right_arr[-1] = height[-1]
        res = 0
        for i in range(1, len(max_left_arr)):
            max_left_arr[i] = max(height[i], max_left_arr[i-1])
        for i in range(n-2, -1, -1):
            max_right_arr[i] = max(height[i], max_right_arr[i+1])
        for i in range(n):
            res += max(min(max_left_arr[i],max_right_arr[i])-height[i], 0)
        return res
