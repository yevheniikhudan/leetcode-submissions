class Solution {
   public:
    int eraseOverlapIntervals(std::vector<std::vector<int>>& intervals) {
        int res = 0;
        sort(intervals.begin(), intervals.end(),
             [](const vector<int>& x, const vector<int>& y) { return x[1] < y[1]; });
        int last = intervals[0][1];

        for (int i = 1; i < intervals.size(); i++) {
            if (intervals[i][0] < last) {
                res++;
            } else {
                last = intervals[i][1];
            }
        }

        return res;
    }
};