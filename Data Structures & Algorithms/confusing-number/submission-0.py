class Solution:
    def confusingNumber(self, n: int) -> bool:
        invertMap = {0: 0, 1: 1, 8: 8, 6: 9, 9: 6}
        invertNumber = 0
        nCopy = n

        while nCopy:
            temp = nCopy % 10
            if temp not in invertMap:
                return False

            invertNumber = invertNumber * 10 + invertMap[temp]
            nCopy //= 10

        return invertNumber != n