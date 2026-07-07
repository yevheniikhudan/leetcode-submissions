class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == "":
            return ""

        n = len(s)
        indices = [0, 0]

        def expand(left, right):
            nonlocal indices

            if s[left] != s[right]:
                return

            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1

            left += 1
            right -= 1

            if right - left + 1 > indices[1] - indices[0] + 1:
                indices = [left, right]

        for i in range(1, n):
            expand(i, i)
            expand(i - 1, i)

        return s[indices[0] : indices[1] + 1]