class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            nextPerms = []

            for p in res:
                for i in range(len(p) + 1):
                    pCopy = p[:]
                    pCopy.insert(i, num)
                    nextPerms.append(pCopy)

            res = nextPerms

        return res