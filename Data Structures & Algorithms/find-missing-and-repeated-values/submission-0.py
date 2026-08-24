from collections import Counter
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        count = {}
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                count[grid[i][j]] = count.get(grid[i][j], 0)+1
        for i in range(1, len(grid)**2+1):
            if i not in count:
                b = i
            elif count[i] == 2:
                a = i
        return [a, b]