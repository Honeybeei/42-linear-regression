from core.Dataset import Dataset
from utils.formatted_io import read_data, get_latest_theta, save_theta, reset_theta
from utils.string_utils import color_string, Color
from core.computation import get_optimized_start, get_trained_thetas, get_cost
from core.constants import CoreConstants
from utils.debug_tool import error_catcher
from numpy import random


@error_catcher
def main():
    """This is the main function"""
    try:
        # prompt user to reset the theta values
        if (
            input(
                color_string(
                    "\nDo you want to reset the theta values? (y/n): ", Color.YELLOW
                )
            ).lower()
            == "y"
        ):
            reset_theta()
        # Get the km and price data
        milages, prices = read_data()
        print(color_string("\nData loaded successfully", Color.GREEN))

        # Create a Dataset object
        dataset = Dataset(milages, prices)
        dataset.print_data()

        learning_rate = CoreConstants.INITIAL_LEARNING_RATE

        initial_theta0 = None
        initial_theta1 = None
        if CoreConstants.STARTING_TYPE == "optimized":
            initial_theta0, initial_theta1 = get_optimized_start(dataset)
        elif CoreConstants.STARTING_TYPE == "random":
            initial_theta0 = random.randint(
                low=CoreConstants.RANDOM_THETA0_MIN,
                high=CoreConstants.RANDOM_THETA0_MAX,
            )
            initial_theta1 = (
                random.rand()
                * (CoreConstants.RANDOM_THETA1_MAX - CoreConstants.RANDOM_THETA1_MIN)
                + CoreConstants.RANDOM_THETA1_MIN
            )
        elif CoreConstants.STARTING_TYPE == "zero":
            initial_theta0 = 0
            initial_theta1 = 0
        else:
            raise ValueError(
                f"Invalid starting type: {CoreConstants.STARTING_TYPE}. Must be one of 'optimized', 'random', or 'zero'"
            )
        save_theta(initial_theta0, initial_theta1)

        print("\nStarting training...")

        saved_theta_count = 0
        previous_cost = None

        # Training loop -> saves trained thetas to a file
        while True:
            # Get the latest thetas
            theta0, theta1 = get_latest_theta("./data/theta.csv")

            # Train the model (get the trained thetas)
            try:
                trained_theta0, trained_theta1 = get_trained_thetas(
                    dataset=dataset,
                    theta0=theta0,
                    theta1=theta1,
                    learning_rate=learning_rate,
                    print_iterations=False,
                )

            # Overshooting handling
            except ValueError as e:
                print(color_string(f"\n{e}", Color.RED))
                learning_rate *= CoreConstants.LEARNING_RATE_DECREASE_FACTOR
                print(
                    color_string(
                        f"Learning rate decreased to {learning_rate}", Color.RED
                    )
                )
                # reset the data(thetas) and continue the training
                reset_theta(initial_theta0, initial_theta1)

                saved_theta_count = 0
                continue

            # Save the trained thetas
            save_theta(trained_theta0, trained_theta1)
            saved_theta_count += 1

            # Check if the training is done
            cost = get_cost(dataset, trained_theta0, trained_theta1)
            if previous_cost is not None:
                cost_diff = abs(cost - previous_cost)
                if cost_diff < CoreConstants.COST_DIFF_THRESHOLD:
                    # training is done
                    print(color_string("\nTraining is done! ", Color.GREEN))
                    print(
                        color_string(
                            f"Optimal theta0: {trained_theta0} | Optimal theta1: {trained_theta1} | Cost: {cost}",
                            Color.BLUE,
                        )
                    )
                    break
                else:
                    color = None
                    if cost_diff > CoreConstants.COST_DIFF_THRESHOLD * 2:
                        color = Color.RED
                    elif cost_diff > CoreConstants.COST_DIFF_THRESHOLD * 1.1:
                        color = Color.PURPLE
                    elif cost_diff > CoreConstants.COST_DIFF_THRESHOLD * 1.01:
                        color = Color.YELLOW
                    elif cost_diff > CoreConstants.COST_DIFF_THRESHOLD * 1.001:
                        color = Color.BLUE
                    else:
                        color = Color.GREEN
                    # training is not done yet
                    print(
                        color_string(
                            f"[{(saved_theta_count - 1):010}] theta0: {trained_theta0:>16.8f} | theta1: {trained_theta1:>16.8f} | cost diff: {cost_diff:>16.8f} | cost: {cost:>16.8f}",
                            color=color,
                        )
                    )
            previous_cost = cost

    except Exception as e:
        print(color_string(f"\nAn error occurred: {e}", Color.RED))
        print(f"\n{color_string(f'Exiting...', Color.RED)}")


if __name__ == "__main__":
    main()
