class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        n = len(candidates)

        def backtrack(i: int, cur: List[int], total):
            if total == target:
                res.append(cur[:])
                return

            for j in range(i, n):
                candidate = candidates[j]

                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                if candidate + total > target:
                    return

                cur.append(candidate)
                backtrack(j + 1, cur, candidate + total)
                cur.pop()

        backtrack(0, [], 0)

        return res