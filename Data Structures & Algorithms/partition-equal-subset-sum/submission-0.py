class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        numsTotal = sum(nums)
        if numsTotal % 2:
            return False
        targetSum = numsTotal // 2
        dp = [False] * (targetSum + 1)
        dp[0] = True

        for num in nums:
            for j in range(targetSum, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[targetSum]