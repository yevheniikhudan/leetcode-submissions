class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]

            if i == len(s):
                return True

            for word in wordDict:
                if s[i:i+len(word)] != word:
                    continue
                
                memo[i] = dfs(i + len(word))
                
                if memo[i]:
                    return True

            return False

        return dfs(0)