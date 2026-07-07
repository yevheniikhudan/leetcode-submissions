class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Find median of two sorted arrays using binary search on partition.

        Args:
            nums1: First sorted array
            nums2: Second sorted array

        Returns:
            Median of combined arrays

        Time Complexity: O(log min(m, n)) - binary search on smaller array
        Space Complexity: O(1) - constant extra space
        """
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            partition_a = left + (right - left) // 2
            partition_b = (m + n + 1) // 2 - partition_a

            max_left_a = nums1[partition_a - 1] if partition_a > 0 else float("-inf")
            max_left_b = nums2[partition_b - 1] if partition_b > 0 else float("-inf")
            min_right_a = nums1[partition_a] if partition_a < m else float("inf")
            min_right_b = nums2[partition_b] if partition_b < n else float("inf")

            if max_left_a > min_right_b:
                right = partition_a - 1
            elif max_left_b > min_right_a:
                left = partition_a + 1
            else:
                if (m + n) % 2 == 0:
                    return (
                        max(max_left_a, max_left_b) + min(min_right_a, min_right_b)
                    ) / 2
                else:
                    return max(max_left_a, max_left_b)
        