class Solution:
    def scoreOfString(self, s: str) -> int:
        codes = [ord(_) for _ in s]
        res = 0

        for i in range(1, len(codes)):
            res += abs(codes[i] - codes[i - 1])

        return res