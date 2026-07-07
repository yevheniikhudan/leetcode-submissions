class Solution:
    def search(self, nums: List[int], target: int) -> int:
        result = -1
        right = len(nums) - 1
        left = 0

        while left <= right:
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            
            if right - left <= 1:
                return -1

            middle = left + (right - left) // 2
            if nums[middle] > target:
                right = middle
            else:
                left = middle


        return result