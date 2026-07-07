class MedianFinder {

    PriorityQueue<Integer> small;
    PriorityQueue<Integer> large;

    public MedianFinder() {
        small = new PriorityQueue<>(Collections.reverseOrder());
        large = new PriorityQueue<>();
    }

    public void addNum(int num) {
        small.offer(num);
        large.offer(small.poll());
        if (large.size() > small.size()) {
            small.offer(large.poll());
        }
    }

    public Double findMedian() {
        if (small.size() > large.size()) {
            return (double)small.peek();
        }

        return (double)(small.peek() + large.peek()) / 2;
    }
}
