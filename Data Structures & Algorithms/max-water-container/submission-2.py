class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0;

        l, r = 0, len(heights) - 1;

        while l < r:
            h_l = heights[l]
            h_r = heights[r]

            max_area = max(max_area, (r - l) * min(h_r, h_l))

            if h_l < h_r:
                l += 1
            else:
                r -= 1

        return max_area;