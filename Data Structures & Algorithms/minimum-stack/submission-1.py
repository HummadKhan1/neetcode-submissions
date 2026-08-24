class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        new_stack = self.stack[:]
        for i in range(len(new_stack)):
            if i == 0:
                minimum = new_stack[i]
            elif new_stack[i] < minimum:
                minimum = new_stack[i]
        return minimum