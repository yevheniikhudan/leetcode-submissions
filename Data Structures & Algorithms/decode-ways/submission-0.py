class Solution:
    def numDecodings(self, s: str) -> int:
        def dfs(i):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0

            res = dfs(i + 1)
            num = int(s[i:i+2])
            if 10 <= num <= 26:
                res += dfs(i + 2)

            return res

        return dfs(0)