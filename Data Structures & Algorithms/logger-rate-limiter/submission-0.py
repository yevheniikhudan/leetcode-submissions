class Logger:

    def __init__(self):
        self.timestamps = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.timestamps or self.timestamps[message] <= timestamp:
            self.timestamps[message] = 10 + timestamp
            return True

        return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
