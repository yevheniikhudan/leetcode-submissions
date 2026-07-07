class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last_index = [0] * 26
        n = len(S)
        partitions = []

        for i in range(n - 1, -1, -1):
            letterIndex = ord(S[i]) - ord("a")
            if last_index[letterIndex] == 0:
                last_index[letterIndex] = i
        end = 0
        start = 0
        for i in range(n):
            end = max(end, last_index[ord(S[i]) - ord("a")])
            if i == end:
                partitions.append(end - start + 1)
                start = i + 1

        return partitions