class Solution:
    def isHappy(self, n: int) -> bool:
        """
        Determine if a number n is a happy number.

        Skeleton: no implementation here. Replace `pass` with actual logic.
        """
        slow, fast = n, n

        while True:
            slow = self.sumOfSquares(slow)
            fast = self.sumOfSquares(self.sumOfSquares(fast))

            # If either pointer reached 1, n is happy.
            if slow == 1 or fast == 1:
                return True

            # If pointers meet at a non-1 value, there's a cycle -> not happy.
            if slow == fast:
                return False

    def sumOfSquares(self, n: int) -> int:
        res = 0
        while n > 0:
            num = n % 10
            res += num**2
            n //= 10
        return res