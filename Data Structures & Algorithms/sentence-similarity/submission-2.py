class Solution:
    def areSentencesSimilar(
        self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]
    ) -> bool:
        """
        Determine if two sentences are similar based on similar word pairs.

        Args:
            sentence1: First sentence as a list of words
            sentence2: Second sentence as a list of words
            similarPairs: List of similar word pairs

        Returns:
            True if sentences are similar, False otherwise
        """

        if len(sentence1) != len(sentence2):
            return False

        pairs = set()
        for w1, w2 in similarPairs:
            pairs.add((w1, w2))
            pairs.add((w2, w1))

        for i in range(len(sentence1)):
            if sentence1[i] == sentence2[i]:
                continue
            if (sentence1[i], sentence2[i]) not in pairs:
                return False

        return True