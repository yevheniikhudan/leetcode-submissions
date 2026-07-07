class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for s in strs:
            counts = [0] * 26
            for ch in s:
                counts[ord(ch) - ord('a')] += 1

            key = tuple(counts)

            if key not in anagrams:
                anagrams[key] = [s]
            else:
                anagrams[key].append(s)

        return list(anagrams.values())