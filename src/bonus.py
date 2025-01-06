from core.Dataset import Dataset
from utils.formatted_io import read_data, get_latest_theta
from utils.string_utils import color_string, Color
from visualizer.Visualizer import Visualizer
from visualizer.Dot import Dot
from visualizer.Line import Line
from utils.terminal_utils import press_any_key
from visualizer.constants import VisualizerConstants
import time
import matplotlib


def main():
    # Get dataset
    x, y = read_data()
    dataset = Dataset(x, y)
    dataset.print_data()
    press_any_key()
    # Read the latest theta values
    theta0, theta1 = get_latest_theta()
    matplotlib.use("Qt5Agg")
    visualizer = Visualizer()
    print("1" * 80)  # TODO: Remove this line

    for i in range(dataset.get_size()):
        dot = Dot(x=dataset.get_milage(i), y=dataset.get_price(i))
        visualizer.add_dot(dot)
    print("2" * 80)  # TODO: Remove this line
    color_index = 0
    while True:
        try:
            new_theta0, new_theta1 = get_latest_theta()
        except ValueError as e:
            print(color_string(f"An error occurred: {e}", Color.RED))
            visualizer.clear(clear_lines=True, clear_dots=False)
            continue
        except Exception as e:
            print(color_string(f"An error occurred: {e}", Color.RED))
            continue
        if new_theta0 != theta0 or new_theta1 != theta1:
            # means the theta has been updated
            time_stamp = time.strftime("%H:%M:%S", time.localtime())
            print(color_string(f"{time_stamp}", Color.YELLOW), end=": ")
            print(
                color_string(f"{theta0:012.6f}, {theta1:012.6f}", Color.BLUE),
                end=" -> ",
            )
            print(
                color_string(f"{new_theta0:012.6f}, {new_theta1:012.6f}", Color.GREEN)
            )
            theta0, theta1 = new_theta0, new_theta1
            line = Line(theta0, theta1, VisualizerConstants.COLORS[color_index])
            visualizer.add_line(line)
            color_index += 1
            if color_index == len(VisualizerConstants.COLORS):
                color_index = 0
            time.sleep(0.01)


if __name__ == "__main__":
    main()
