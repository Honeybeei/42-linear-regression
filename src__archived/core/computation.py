from .constants import CoreConstants
from typing import Tuple
from core.Dataset import Dataset


def get_price(milage: float, theta0: float, theta1: float) -> float:
    """Calculate the price of a car based on its milage and thetas

    Args:
        milage (float): milage of the car
        theta0 (float): bias
        theta1 (float): weight

    Returns:
        float: the price of the car
    """
    return theta0 + theta1 * milage


def get_cost(data: Dataset, theta0: float, theta1: float) -> float:
    """Calculate the cost of the model based on the data and thetas

    Args:
        data (Dataset): the dataset object
        theta0 (float): bias
        theta1 (float): weight

    Returns:
        float: the cost of the model
    """
    m = data.get_size()
    cost = 0
    for i in range(m):
        x = data.get_milage(i)
        y = data.get_price(i)
        cost += (theta0 + theta1 * x - y) ** 2
    return cost / (2 * m)


def get_trained_thetas(
    dataset: Dataset,
    theta0: float,
    theta1: float,
    learning_rate: float,
    iterations: int = CoreConstants.ITERATIONS,
    print_iterations: bool = False,
) -> Tuple[float, float]:
    """Get the trained thetas based on the data and the initial thetas

    Args:
        data (Dataset): the dataset object
        theta0 (float): initial theta0
        theta1 (float): initial theta1

    Raises:
        ValueError: if the gradient is nan (overshooting)

    Returns:
        Tuple[float, float]: trained thetas
    """
    previous_cost = None
    for i in range(iterations):
        grad0, grad1 = get_gradients(dataset, theta0, theta1)

        # Check if the cost is increasing
        cost = get_cost(dataset, theta0, theta1)
        if previous_cost is not None and cost > previous_cost:
            raise ValueError("Overshooting detected: cost increased.")
        previous_cost = cost
        if CoreConstants.USE_THETA0_ACCELERATION:
            new_theta0 = (
                theta0 - learning_rate * grad0 * CoreConstants.THETA0_ACCELERATION_RATE
            )
        else:
            new_theta0 = theta0 - learning_rate * grad0
        new_theta1 = theta1 - learning_rate * grad1
        if print_iterations and i % CoreConstants.ITERATION_PRINT_INTERVAL == 0:
            print(f"\nIteration {i + 1}")
            print(f"Gradient0: {grad0}")
            print(f"Gradient1: {grad1}")
            print(f"Theta0   : {theta0} -> {new_theta0}")
            print(f"Theta1   : {theta1} -> {new_theta1}")
        theta0 = new_theta0
        theta1 = new_theta1
    return theta0, theta1


def get_gradients(data, theta0, theta1):
    m = data.get_size()
    grad0 = 0
    grad1 = 0
    for i in range(m):
        x = data.get_milage(i)
        y = data.get_price(i)
        grad0 += (theta0 + theta1 * x) - y
        grad1 += ((theta0 + theta1 * x) - y) * x
    grad0 /= m
    grad1 /= m
    return grad0, grad1


def get_optimized_start(data: Dataset) -> Tuple[float, float]:
    """Get the optimized start thetas for the training

    Args:
        data (Dataset): the dataset object

    Returns:
        Tuple[float, float]: the optimized thetas
    """
    first_milage_price = data.get_milage(0), data.get_price(0)
    last_milage_price = data.get_milage(data.get_size() - 1), data.get_price(
        data.get_size() - 1
    )
    theta1 = (last_milage_price[1] - first_milage_price[1]) / (
        last_milage_price[0] - first_milage_price[0]
    )
    theta0 = first_milage_price[1] - theta1 * first_milage_price[0]
    return theta0, theta1
