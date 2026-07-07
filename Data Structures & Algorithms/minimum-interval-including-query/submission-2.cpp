class Solution {
   public:
    std::vector<int> minInterval(std::vector<std::vector<int>>& intervals,
                                 std::vector<int>& queries) {
        sort(intervals.begin(), intervals.end());
        std::vector<int> sortedQueries = queries;
        sort(sortedQueries.begin(), sortedQueries.end());
        int i = 0;
        std::unordered_map<int, int> minIntervals;
        std::vector<int> res;
        std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>,
                            std::greater<std::pair<int, int>>>
            pq;
        for (int query : sortedQueries) {
            while (i < intervals.size() && intervals[i][0] <= query) {
                pq.push({intervalSize(intervals[i]), intervals[i][1]});
                i++;
            }

            while (pq.size() > 0 && pq.top().second < query) {
                pq.pop();
            }

            minIntervals[query] = pq.size() > 0 ? pq.top().first : -1;
        }

        for (int query : queries) {
            res.push_back(minIntervals[query]);
        }
        return res;
    }

   private:
    int intervalSize(std::vector<int>& interval) { return interval[1] - interval[0] + 1; }
};
