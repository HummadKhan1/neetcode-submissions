class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        curRow = []

        for i in range(numRows):
            curRow = []
            if i == 0:
                res.append([1])
            elif i == 1:
                res.append([1,1])
            else:
                prevRow = res[-1]
                curValue = prevRow[0]
                new_list = [1]
                for j in range(1, len(prevRow)):
                    curValue += prevRow[j]
                    new_list.append(curValue)
                    curValue -= prevRow[j-1]
                new_list.append(1)
                res.append(new_list)
        return res
