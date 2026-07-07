class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        leftShifts = 0

        for d, a in shift:
            if d == 1:
                leftShifts -= a
            else:
                leftShifts += a

        leftShifts %= len(s)
        return s[leftShifts:] + s[:leftShifts]