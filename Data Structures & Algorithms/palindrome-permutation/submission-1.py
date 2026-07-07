class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        chars = set()

        for ch in s:
            if ch in chars:
                chars.remove(ch)
            else:
                chars.add(ch)
        return len(chars) <= 1