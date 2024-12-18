import matplotlib.pyplot as plt
from typing import List, Tuple
import numpy as np
from utils.debug_tool import error_catcher


@error_catcher
def display_dots(data: List[Tuple[float, float]], color: str = "blue"):
    x = [d[0] for d in data]
    y = [d[1] for d in data]
    # print dots
    plt.scatter(x, y, label="Data", color=color)
    plt.title("Data")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()
    plt.show()


@error_catcher
def display_lines(lines: List[Tuple[float, float]]):
    colors = ["red", "green", "blue", "purple", "orange", "black"]
    color_index = 0
    for line in lines:
        x = np.linspace(-10, 10, 400)
        y = line[0] * x + line[1]
        plt.plot(x, y, label=f"y = {line[0]}x + {line[1]}", color=colors[color_index])
        color_index += 1
        if color_index == len(colors):
            color_index = 0
    plt.title("Lines")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()
    plt.show()


@error_catcher
def display_dots_and_lines(
    data: List[Tuple[float, float]], lines: List[Tuple[float, float]]
):
    x = [d[0] for d in data]
    y = [d[1] for d in data]
    # print dots
    plt.scatter(x, y, label="Data", color="blue")
    colors = ["red", "green", "blue", "purple", "orange", "black"]
    color_index = 0
    for line in lines:
        x = np.linspace(-10, 10, 400)
        y = line[0] * x + line[1]
        plt.plot(x, y, label=f"y = {line[0]}x + {line[1]}", color=colors[color_index])
        color_index += 1
    plt.title("Data and Lines")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()
    plt.show()
