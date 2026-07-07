class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        res, cur, total = 0, 0, 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]

            total += diff
            cur += diff
            if cur < 0:
                res = i + 1
                cur = 0

        return -1 if total < 0 else res