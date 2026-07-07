class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        cache = []

        for pos, spd in cars:
            time = (target - pos) / spd

            if not cache or time > cache[-1]:
                cache.append(time)

        return len(cache)