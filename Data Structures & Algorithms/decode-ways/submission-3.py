class Solution:
    def numDecodings(self, s: str) -> int:
        dpI, dpIMinus1, dpIMinus2 = 1, 1, 1

        for i in range(1, len(s) + 1):
            dpI = 0 if s[i - 1] == "0" else dpIMinus1

            if i >= 2 and 10 <= int(s[i - 2 : i]) <= 26:
                dpI += dpIMinus2
                
            dpIMinus2, dpIMinus1 = dpIMinus1, dpI

        return dpI