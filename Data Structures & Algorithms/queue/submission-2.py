class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
class Deque:
    
    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        if self.head.next == self.tail:
            return True
        return False
        
    def append(self, value: int) -> None:
        newNode, next, prev = ListNode(value), self.tail, self.tail.prev
        prev.next = newNode
        next.prev = newNode
        newNode.next = next
        newNode.prev = prev
        

    def appendleft(self, value: int) -> None:
        newNode, next, prev = ListNode(value), self.head.next, self.head
        prev.next = newNode
        next.prev = newNode
        newNode.next = next
        newNode.prev = prev

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        prev, next, popped = self.tail.prev.prev, self.tail, self.tail.prev
        prev.next = next
        next.prev = prev
        return popped.val
        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        popped, next, prev = self.head.next, self.head.next.next, self.head
        prev.next = next
        next.prev = prev
        return popped.val
