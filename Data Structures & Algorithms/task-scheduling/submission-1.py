class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counters = Counter(tasks)
        maxHeap = [-cnt for cnt in counters.values()]
        heapq.heapify(maxHeap)
        q = deque()
        time = 0

        while maxHeap or q:
            time += 1
            if not maxHeap:
                time = q[0][1]
            else:
                cnt = -heapq.heappop(maxHeap) - 1
                if cnt:
                    q.append([cnt, time + n])

            if q and q[0][1] <= time:
                heapq.heappush(maxHeap, -q.popleft()[0])

        return time
