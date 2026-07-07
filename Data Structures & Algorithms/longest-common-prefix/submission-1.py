# Vertical Scanning

# Intuition
# Instead of comparing entire strings horizontally, we can compare characters column by column across all strings. Check if all strings have the same character at position 0, then position 1, and so on. The moment we find a mismatch or reach the end of any string, we've found where the common prefix ends.

# Algorithm
# Iterate through character positions starting from index 0.
# At each position i, check the character in the first string.
# Compare this character against position i in every other string.
# If any string is too short or has a different character, return the prefix up to index i-1.
# If we complete the loop without returning, the entire first string is the common prefix.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for j in range(len(strs[0])):
            for i in range(1, len(strs)):
                if j == len(strs[i]) or strs[0][j] != strs[i][j]:
                    return strs[0][:j]

        return strs[0]