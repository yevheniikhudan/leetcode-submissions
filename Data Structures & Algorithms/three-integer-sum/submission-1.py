class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = set()

        for i in range(n - 2):
            num_i = nums[i]

            if (i > 0 and nums[i] == nums[i - 1]):
                continue

            seen = set()
            for j in range(i + 1, n):
                num_j = nums[j]
                target = -(num_i + num_j)
                if target in seen:
                    res.add((num_i, num_j, target))

                seen.add(num_j)
        return [list(triplet) for triplet in res]