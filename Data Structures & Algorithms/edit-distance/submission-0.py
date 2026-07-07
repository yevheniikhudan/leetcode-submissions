class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}

        def dfs(i, j):
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            if (i, j) in memo:
                return memo[(i, j)]

            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)

            res = min(1 + dfs(i + 1, j + 1), 1 + dfs(i + 1, j), 1 + dfs(i, j + 1))
            memo[(i, j)] = res
            return res

        return dfs(0, 0)