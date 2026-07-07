class Solution:
    def isHappy(self, n: int) -> bool:
        """
        Determine if a number n is a happy number.

        Skeleton: no implementation here. Replace `pass` with actual logic.
        """
        seen = set()

        while n != 1:
            n = self.sumOfSquares(n)
            if n in seen:
                return False
            seen.add(n)

        return True

    def sumOfSquares(self, n: int) -> int:
        res = 0
        while n > 0:
            num = n % 10
            res += num**2
            n //= 10
        return res