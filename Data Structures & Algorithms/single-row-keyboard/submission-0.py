class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        indices = {}
        for index, ch in enumerate(keyboard):
            indices[ch] = index

        ans = indices[word[0]]
        for i in range(1, len(word)):
            ans += abs(indices[word[i - 1]] - indices[word[i]])
        return ans