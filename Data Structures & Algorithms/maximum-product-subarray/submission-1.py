class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxSoFar = 1
        minSoFar = 1
        result = nums[0]

        for num in nums:
            nextMax = num * maxSoFar
            nextMin = num * minSoFar
            maxSoFar = max(num, nextMax, nextMin)
            minSoFar = min(num, nextMax, nextMin)
            result = max(result, maxSoFar)

        return result