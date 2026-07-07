class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        result = 0
        x = abs(x)
        while x:
            result *= 10
            result += x % 10
            x //= 10
            if result > 2**31 - 1:
                return 0
        return sign * result