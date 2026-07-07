class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max = 0
        right_max = 0
        res = 0

        while (left < right):
            h_l, h_r = height[left], height[right]
            if h_l < h_r:
                left_max = max(left_max, h_l)
                res += left_max - h_l
                left += 1
            else:
                right_max = max(right_max, h_r)
                res += right_max - h_r
                right -= 1
        return res