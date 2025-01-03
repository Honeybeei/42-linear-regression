import math
from typing import List
from .Dot import Dot
from .constants import VisualizerConstants


class Line:
    def __init__(
        self, theta0: float, theta1: float, color: str = VisualizerConstants.COLORS[0]
    ) -> None:
        self.theta0 = theta0
        self.theta1 = theta1
        self.color = color

    @classmethod
    def from_dots(cls, dot1: Dot, dot2: Dot, color: str) -> "Line":
        line = cls(0, 0, color)
        line.set_theta(dot1, dot2)
        return line

    def __str__(self) -> str:
        return f"y = {self.theta0} + {self.theta1}x with color {self.color}"

    def __eq__(self, other: "Line") -> bool:
        return self.theta0 == other.theta0 and self.theta1 == other.theta1

    def get_y(self, x: float) -> float:
        return self.theta0 + self.theta1 * x

    def get_x(self, y: float) -> float:
        return (y - self.theta0) / self.theta1

    def get_y_intercept(self) -> float:
        if math.isinf(self.theta1):
            return None
        return self.get_y(0)

    def get_x_intercept(self) -> float:
        if self.theta1 == 0:
            return None
        return self.get_x(0)

    def set_theta(self, dot1: Dot, dot2: Dot) -> None:
        self.theta1 = (dot2.y - dot1.y) / (dot2.x - dot1.x)
        self.theta0 = dot1.y - self.theta1 * dot1.x

    def get_points_for_drawing(self, x_min: float, x_max: float) -> List[Dot]:
        return [Dot(x, self.get_y(x)) for x in range(int(x_min), int(x_max) + 1)]

    def get_points(self, point_count: int = 2) -> List[Dot]:
        """Get a list of points on the line. The default is 2 points(x intercept and y intercept)

        Args:
            point_count (int, optional): The number of points to be returned. Defaults to 2

        Raises:
            ValueError: If point_count is less than 2

        Returns:
            List[Tuple[float, float]]: A list of points on the line
        """
        if point_count < 2:
            raise ValueError("point_count must be at least 2")
        list_of_points: List[Dot] = []
        x_intercept = Dot(x=self.get_x_intercept(), y=0)
        y_intercept = Dot(x=0, y=self.get_y_intercept())
        if x_intercept.x is None:
            # horizontal line
            x_intercept.x = self.get_y_intercept()
        elif y_intercept.y is None:
            # vertical line
            y_intercept.y = self.get_x_intercept()
        list_of_points.append(x_intercept)
        list_of_points.append(y_intercept)
        if point_count > 2:
            # get additional points
            gap_between_x = abs(x_intercept.x - y_intercept.x) / (point_count - 1)
            for i in range(1, point_count - 1):
                x = x_intercept.x + i * gap_between_x
                y = self.get_y(x)
                list_of_points.append(Dot(x, y))
        return list_of_points
