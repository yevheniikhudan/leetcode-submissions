class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, res = 0, 0
        seen = {}

        for right, ch in enumerate(s):
            if ch in seen:
                left = max(seen[ch] + 1, left)

            seen[ch] = right
            res = max(res, right - left + 1)

        return res