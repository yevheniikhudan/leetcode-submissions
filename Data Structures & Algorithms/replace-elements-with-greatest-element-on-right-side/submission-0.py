class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max = arr[-1]
        arr[-1] = -1

        for i in range(len(arr) - 2, -1, -1):
            temp = arr[i]
            arr[i] = max
            if temp > max:
                max = temp

        return arr