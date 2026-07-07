class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums)

        def dfs(i):
            if (i) in memo:
                return memo[i]
            if i == len(nums):
                return 0

            res = 1

            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    res = max(res, 1 + dfs(j))

            memo[i] = res
            return res

        return max(dfs(i) for i in range(n))