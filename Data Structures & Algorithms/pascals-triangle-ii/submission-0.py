class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        lastRow = [1]

        for i in range(rowIndex):
            curRow = [0] + lastRow + [0]
            newRow = []
            for j in range(1, len(curRow)):
                newRow.append(curRow[j] + curRow[j-1])
            lastRow = newRow
        return lastRow
