import math
from typing import List, Tuple
from .constants import VisualizerConstants


class Dot:
    def __init__(
        self, x: float, y: float, color: str = VisualizerConstants.COLORS[0]
    ) -> None:
        self.x = x
        self.y = y
        self.color = color

    def __str__(self) -> str:
        return f"({self.x}, {self.y}) with color {self.color}"

    def __eq__(self, other: "Dot") -> bool:
        return self.x == other.x and self.y == other.y

    @staticmethod
    def distance(dot1: "Dot", dot2: "Dot") -> float:
        return math.sqrt((dot1.x - dot2.x) ** 2 + (dot1.y - dot2.y) ** 2)

    @staticmethod
    def from_points(points: List[Tuple[float, float]], color: str) -> List["Dot"]:
        return [Dot(x, y, color) for x, y in points]
