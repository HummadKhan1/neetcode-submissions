class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dArr = [-1]*capacity
        self.length = 0

    def get(self, i: int) -> int:
        return self.dArr[i]

    def set(self, i: int, n: int) -> None:
        self.dArr[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        self.dArr[self.length] = n
        self.length += 1

    def popback(self) -> int:
        if self.length > 0:
            self.length -= 1
        return self.dArr[self.length]

    def resize(self) -> None:
        new_arr = [-1]*self.capacity
        self.dArr += new_arr
        self.capacity = self.capacity*2

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity