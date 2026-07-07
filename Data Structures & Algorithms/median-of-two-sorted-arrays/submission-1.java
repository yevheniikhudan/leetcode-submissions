class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
                int m = nums1.length, n = nums2.length;

        if (m > n) {
            return findMedianSortedArrays(nums2, nums1);
        }

        int left = 0, right = m;

        while (left <= right) {
            int partition_a = (left + right) / 2;
            int partition_b = (m + n + 1) / 2 - partition_a;
            int max_left_a = partition_a > 0 ? nums1[partition_a - 1] : Integer.MIN_VALUE;
            int max_left_b = partition_b > 0 ? nums2[partition_b - 1] : Integer.MIN_VALUE;
            int min_right_a = partition_a < m ? nums1[partition_a] : Integer.MAX_VALUE;
            int min_right_b = partition_b < n ? nums2[partition_b] : Integer.MAX_VALUE;

            if (max_left_a <= min_right_b && max_left_b <= min_right_a) {
                if ((m + n) % 2 == 0) {
                    return (double)(Math.max(max_left_a, max_left_b) + Math.min(min_right_a, min_right_b)) / 2;
                } else {
                    return Math.max(max_left_a, max_left_b);
                }
            }

            if (max_left_a > min_right_b) {
                right = partition_a - 1;
            } else {
                left = partition_a + 1;
            }
        }

        return 0.0;
    }
}
