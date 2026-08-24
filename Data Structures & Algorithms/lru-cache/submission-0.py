class LRUCache:

    def __init__(self, capacity: int):
        self.hashmap ={}
        self.capacity = capacity
        self.arr = []

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.arr.remove(key)
            self.arr.append(key)
            return self.hashmap[key]
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.hashmap[key] = value
            self.arr.remove(key)
            self.arr.append(key)
        else:
            self.hashmap[key] = value
            if len(self.arr) >= self.capacity:
                del self.hashmap[self.arr[0]]
                self.arr.remove(self.arr[0])
            self.arr.append(key)
        

