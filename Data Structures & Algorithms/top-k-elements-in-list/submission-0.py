class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counters = {}
        buckets = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            counters[num] = 1 + counters.get(num, 0)

        for num, count in counters.items():
            buckets[count].append(num)

        res = []
        for item in buckets[::-1]:
            for num in item:
                res.append(num)

            if len(res) == k:
                return res

        return res