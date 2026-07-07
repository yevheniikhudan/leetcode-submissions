class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        n = len(words)

        for row in range(n):
            m = len(words[row])
            for col in range(m):
                if (
                    col >= n
                    or row >= len(words[col])
                    or words[row][col] != words[col][row]
                ):
                    return False

        return True