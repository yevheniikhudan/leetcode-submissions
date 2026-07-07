class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        
        n = len(s)
        dp = [1] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = 0 if s[i - 1] == '0' else dp[i - 1]          

            if i >= 2 and 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i - 2]


        return dp[n]