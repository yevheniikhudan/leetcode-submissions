class Solution:
    def countElements(self, arr: List[int]) -> int:
        counts = set(arr)
        res = 0

        for num in arr:
            if (num + 1) in counts:
                res += 1

        return res
