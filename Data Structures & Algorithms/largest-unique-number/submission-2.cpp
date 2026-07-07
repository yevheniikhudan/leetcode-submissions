class Solution {
   public:
    int largestUniqueNumber(vector<int>& nums) {
        unordered_map<int, int> counts;

        for (int num : nums) {
            counts[num] += 1;
        }

        int maxNumber = -1;

        for (const auto& [key, value] : counts) {
            if (value == 1) maxNumber = max(maxNumber, key);
        }

        return maxNumber;
    }
};
