class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        curRow = []
        for i in range(numRows-1):
            curRow = [0] + res[-1] + [0]
            temp = []
            for j in range(1, len(curRow)):
                temp.append(curRow[j]+curRow[j-1])
            res.append(temp)
        return res