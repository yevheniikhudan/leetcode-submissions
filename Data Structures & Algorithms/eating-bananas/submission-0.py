class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        result = right

        def canFinish(speed):
            hours = 0

            for pile in piles:
                hours += math.ceil(float(pile) / speed)

            return hours <= h

        while left <= right:
            mid = left + (right - left) // 2

            if canFinish(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result