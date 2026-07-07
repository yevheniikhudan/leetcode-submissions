class Solution:
    def largestUniqueNumber(self, nums: list[int]) -> int:
        counts = Counter(nums)

        uniqueNums = [num for num, freq in counts.items() if freq == 1]
        return max(uniqueNums) if uniqueNums else -1