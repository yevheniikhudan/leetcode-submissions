class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            num = nums[i]
            x = target - num

            if x in seen:
                return [seen[x], i]

            seen[num] = i

        return [-1, -1]


        