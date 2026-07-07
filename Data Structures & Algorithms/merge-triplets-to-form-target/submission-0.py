class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        first, second, third = False, False, False

        for a, b, c in triplets:
            first = first or (a == target[0] and b <= target[1] and c <= target[2])
            second = second or (b == target[1] and a <= target[0] and c <= target[2])
            third = third or (c == target[2] and a <= target[0] and b <= target[1])

        return first and second and third