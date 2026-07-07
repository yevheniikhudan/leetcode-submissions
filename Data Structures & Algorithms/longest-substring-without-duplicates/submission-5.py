class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        res = 0

        for right, ch in enumerate(s):
            if ch in seen:
                left = max(left, seen[ch] + 1)

            res = max(res, right - left + 1)
            seen[ch] = right

        return res