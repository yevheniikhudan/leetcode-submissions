class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        result = [0] * n

        for index, temperature in enumerate(temperatures):
            while stack and temperatures[index] > temperatures[stack[-1]]:
                stack_index = stack.pop()
                result[stack_index] = index - stack_index

            stack.append(index)

        return result