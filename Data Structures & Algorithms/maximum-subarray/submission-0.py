class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        curSum = 0

        for num in nums:
            curSum += num
            maxSum = max(maxSum, curSum)
            curSum = max(0, curSum)

        return maxSum