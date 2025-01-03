from typing import List
import matplotlib.pyplot as plt
from .Dot import Dot
from .Line import Line
from .constants import VisualizerConstants


class Visualizer:
    def __init__(self):
        plt.ion()
        self.fig, self.ax = plt.subplots()
        self.dots: List[Dot] = []
        self.lines: List[Line] = []

    def close(self):
        plt.ioff()
        plt.show()

    def add_dot(self, dot: Dot):
        self.dots.append(dot)
        self.replot()
        plt.draw()
        plt.pause(VisualizerConstants.PAUSE_TIME)

    def add_line(self, line: Line):
        self.lines.append(line)
        self.replot()
        plt.draw()
        plt.pause(VisualizerConstants.PAUSE_TIME)

    def clear(self, clear_lines=False, clear_dots=False):
        self.ax.clear()
        if clear_lines:
            self.lines = []
        if clear_dots:
            self.dots = []
        self.replot()
        plt.draw()
        plt.pause(VisualizerConstants.PAUSE_TIME)

    def replot(self):
        self.ax.clear()
        for dot in self.dots:
            self.ax.plot(dot.x, dot.y, "o", color=dot.color)
        for line in self.lines:
            points = line.get_points_for_drawing(
                VisualizerConstants.MIN_X, VisualizerConstants.MAX_X
            )
            x_values = [point.x for point in points]
            y_values = [point.y for point in points]
            self.ax.plot(x_values, y_values, color=line.color)
