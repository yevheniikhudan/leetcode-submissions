class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0

        adjList = collections.defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                adjList[self._pattern(word, i)].append(word)

        result = 1
        visited = set([beginWord])
        q = deque([beginWord])

        while q:
            for _ in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return result

                for i in range(len(word)):
                    pattern = self._pattern(word, i)

                    for adj in adjList[pattern]:
                        if adj not in visited:
                            q.append(adj)
                            visited.add(adj)

            result += 1

        return 0


    def _pattern(self, word, i):
        return word[:i] + '*' + word[i+1:]
