class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        
        def canFinish(speed):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / speed)  # No float() needed
            return hours <= h
        
        while left < right:
            mid = left + (right - left) // 2
            
            if canFinish(mid):
                right = mid
            else:
                left = mid + 1
        
        return left