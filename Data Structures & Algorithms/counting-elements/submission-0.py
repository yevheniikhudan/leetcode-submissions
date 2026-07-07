class Solution:
    def countElements(self, arr: List[int]) -> int:
        counts = Counter(arr)
        res = 0

        for num in arr:
            if (num + 1) in counts:
                counts[num + 1] -= 1
                res += 1

        return res
