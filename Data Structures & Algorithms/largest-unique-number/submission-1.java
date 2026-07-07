class Solution {

    public int largestUniqueNumber(int[] nums) {
        Map<Integer, Integer> counts = new HashMap<>();
        for (int num : nums) {
            counts.put(num, counts.getOrDefault(num, 0) + 1);
        }
        int max = -1;

        for (int key : counts.keySet()) {
            if (counts.get(key) == 1) max = Math.max(max, key);
        }
        return max;
    }
}