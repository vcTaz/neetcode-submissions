class DynamicArray:
    
    def __init__(self, capacity: int):
        if capacity > 0:
            self.capacity = capacity
            self.length = 0
            self.array = [0] * capacity

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.length < self.capacity:
            self.array[self.length] = n
            self.length = self.length + 1 
        else:
            self.resize()
            self.array[self.length] = n
            self.length = self.length + 1 

    def popback(self) -> int:
        if self.length > 0:
            retval = self.array[self.length - 1]
            self.array[self.length - 1] = 0
            self.length = self.length - 1
            return retval 
        
        return 0

    def resize(self) -> None:
        self.capacity = self.capacity * 2
        temp = [0] * self.capacity
        temp[:len(self.array)] = self.array[:]
        self.array = temp

    def getSize(self) -> int:
        return self.length 
    
    def getCapacity(self) -> int:
        return self.capacity
