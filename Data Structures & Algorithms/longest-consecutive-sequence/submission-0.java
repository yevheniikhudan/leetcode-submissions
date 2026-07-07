class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }

        Set<Integer> cache = new HashSet<>();
        for (int num : nums) {
            cache.add(num);
        }

        int result = 0;

        for (int num : cache) {
            if (cache.contains(num - 1)) {
                continue;
            }

            int cur = 1;
            while(cache.contains(num + cur)) {
                cur += 1;
            }
            result = Math.max(result, cur);
        }

        return result;
    }
}
