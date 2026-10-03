class MovingAverage:
    # challenges to solve:
    # store array of size n, where you can remove from the start
    # and push to the end in constant time LinkedList?
    # queue will work here
    def __init__(self, size: int):
        self.values = collections.deque()
        self.currentSum = 0
        self.size = size
        self.currentSize = 0

    def next(self, val: int) -> float:
        self.values.append(val)
        self.currentSum += val
        self.currentSize += 1
        
        if self.currentSize > self.size:
            leftValue = self.values.popleft()
            self.currentSum -= leftValue
            self.currentSize -= 1

        return self.currentSum / self.currentSize


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
