class Solution {
    class PQElement {
        int intervalSize;
        int rightIndex;

        public PQElement(int intervalSize, int rightIndex) {
            this.intervalSize = intervalSize;
            this.rightIndex = rightIndex;
        }
    }

    public int[] minInterval(int[][] intervals, int[] queries) {
        Arrays.sort(intervals, Comparator.comparingInt(x -> x[0]));
        int[] sortedQueries = Arrays.copyOf(queries, queries.length);
        Arrays.sort(sortedQueries);

        Map<Integer, Integer> minIntervals = new HashMap<>();
        PriorityQueue<PQElement> pq = new PriorityQueue<>((a, b) -> a.intervalSize - b.intervalSize);
        int i = 0;
        for (int query : sortedQueries) {
            while (i < intervals.length && intervals[i][0] <= query) {
                pq.offer(new PQElement(intervalSize(intervals[i]), intervals[i][1]));
                i++;
            }
            while (pq.size() > 0 && pq.peek().rightIndex < query) {
                pq.poll();
            }
            minIntervals.put(query, pq.size() > 0 ? pq.peek().intervalSize : -1);
        }

        int[] res = new int[queries.length];
        for (int j = 0; j < queries.length; j++) {
            res[j] = minIntervals.get(queries[j]);
        }
        return res;
    }

    private int intervalSize(int[] interval) {
        return interval[1] - interval[0] + 1;
    }
}
