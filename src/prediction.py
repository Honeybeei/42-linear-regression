from enum import Enum
from utils import color_string, Color, get_latest_theta
from core import get_price, Dataset, get_cost
from utils.formatted_io import read_data
from utils.terminal_utils import clear_terminal, display_exit_countdown, press_any_key


class MenuChoice(Enum):
    PREDICT = "1"
    CALCULATE_PRECISION = "2"
    EXIT = "3"


def predict():
    clear_terminal()

    # Get the milage from the user
    while True:
        try:
            milage = float(
                input(
                    color_string(
                        "Enter milage (in km): ",
                        Color.BOLD,
                    ),
                ),
            )
            break
        except ValueError:
            # If the user enters a non-numeric value (error thrown from float())
            print(
                color_string(
                    "Invalid input. Please enter a number",
                    Color.RED,
                ),
            )

    print("Predicting...")

    # Get the latest theta values
    theta0, theta1 = get_latest_theta("./data/theta.csv")
    print(f"Theta0: {theta0}, Theta1: {theta1}")

    # Get the estimated price
    estimated_price = get_price(milage, theta0, theta1)
    print(f"Estimated price: {estimated_price}")


def calculate_precision():
    milages, prices = read_data()
    dataset = Dataset(milages, prices)
    dataset.print_data()
    theta0, theta1 = get_latest_theta()
    cost = get_cost(dataset, theta0, theta1)
    print("How cost is calculated: ")
    print(
        "Cost: The sum of the square of the difference between the predicted value and the actual value"
    )
    print(f"\nTheta0  : {theta0}")
    print(f"Theta1  : {theta1}")
    print(f"Cost    : {cost}")
    print("\nYou can check the cost decrease when you train the model.")
    print("")


def main():
    try:
        while True:
            clear_terminal()
            # prompt user for input
            menu = f"""
{color_string("Welcome to the prediction system", Color.BOLD)}

[1] {color_string("Predict", Color.GREEN)}
[2] {color_string("Calculate precision", Color.YELLOW)}
[3] {color_string("Exit", Color.BLUE)}
"""
            print(menu)
            choice = input(color_string("Enter choice: ", Color.BOLD))
            if choice == MenuChoice.PREDICT.value:
                predict()
                press_any_key()
            elif choice == MenuChoice.CALCULATE_PRECISION.value:
                calculate_precision()
                press_any_key()
            elif choice == MenuChoice.EXIT.value:
                display_exit_countdown(3)
                exit(0)
            else:
                print(color_string("Invalid choice", Color.RED))
                press_any_key()
    except Exception as e:
        print(color_string(f"\nAn error occurred: {e}", Color.RED))
        print(f"\n{color_string(f'Exiting...', Color.RED)}")


if __name__ == "__main__":
    main()
