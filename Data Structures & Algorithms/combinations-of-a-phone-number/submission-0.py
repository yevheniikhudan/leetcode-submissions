class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        numbersToLetters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(index, s):
            if len(s) == len(digits):
                res.append(s)
                return

            for c in numbersToLetters[digits[index]]:
                dfs(index + 1, s + c)

        if digits:
            dfs(0, "")

        return res