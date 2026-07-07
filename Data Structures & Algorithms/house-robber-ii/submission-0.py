class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def rob(left: int, right: int) -> int:  # rob left inclusive right exclusive
            a, b = 0, 0
            for i in range(left, right):
                a, b = b, max(nums[i] + a, b)

            return b

        return max(rob(0, n - 1), rob(1, n))  