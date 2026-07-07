class Solution:
    def checkValidString(self, s: str) -> bool:
        low, heigh = 0, 0

        for ch in s:
            if ch == "(":
                low += 1
                heigh += 1
            elif ch == ")":
                low = max(0, low - 1)
                heigh -= 1
            else:
                low = max(0, low - 1)
                heigh += 1

            if heigh < 0:
                return False

        return low == 0