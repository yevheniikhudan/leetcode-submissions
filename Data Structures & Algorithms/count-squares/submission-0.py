class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)
        self.x_coords = defaultdict(set)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[(x, y)] += 1
        self.x_coords[x].add(y)

    def count(self, point: List[int]) -> int:
        px, py = point
        result = 0

        for y in self.x_coords[px]:
            if py == y:
                continue

            side = abs(py - y)
            # Frequency of the vertical point (same x-coordinate)
            freq_vert = self.points[(px, y)]

            if (px + side, py) in self.points and (px + side, y) in self.points:
                result += freq_vert * self.points[(px + side, py)] * self.points[(px + side, y)]

            if (px - side, py) in self.points and (px - side, y) in self.points:
                result += freq_vert * self.points[(px - side, py)] * self.points[(px - side, y)]

        return result
