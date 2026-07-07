class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = {}

        for index, num in enumerate(nums2):
            mapping[num] = index

        res = []

        for num in nums1:
            res.append(mapping[num])

        return res