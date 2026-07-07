class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        q = deque()

        for right, right_num in enumerate(nums):
            while q and q[0] <= right - k:
                q.popleft()

            while q and nums[q[-1]] < right_num:
                q.pop()

            q.append(right)

            if right + 1 >= k:
                result.append(nums[q[0]])

        return result
        