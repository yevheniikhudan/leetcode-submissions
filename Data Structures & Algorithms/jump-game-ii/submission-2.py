class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        far = 0
        cur = 0
        jumps = 0

        for i in range(len(nums)):
            far = max(far, i + nums[i])

            if i == cur:
                cur = far
                jumps += 1

            if cur >= len(nums) -1:
                break

        return jumps