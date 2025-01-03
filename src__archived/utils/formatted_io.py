import os
from typing import List, Tuple, TextIO
from .constants import IOConstants

DATA_FILE_PATH = os.path.join(IOConstants.DATA_DIR, IOConstants.DATA_FILE)
THETA_FILE_PATH = os.path.join(IOConstants.DATA_DIR, IOConstants.THETA_FILE)


def check_header(file: TextIO, expected_header: List[str]):
    """Check if the header of the file matches the expected header.

    Args:
        file (TextIO): file object
        expected_header (List[str]): List of expected headers

    Raises:
        ValueError: Header length mismatch
        ValueError: Header content mismatch
    """
    first_line = file.readline()
    header = first_line.strip().split(",")
    if len(expected_header) != len(header):
        raise ValueError("Header length mismatch")
    for actual, expected in zip(header, expected_header):
        if actual.strip().lower() != expected.strip().lower():
            raise ValueError(
                f"Header content mismatch: expected '{expected}', got '{actual}'"
            )


def read_data(path: str = DATA_FILE_PATH) -> Tuple[List[float], List[float]]:
    """Reads data from a CSV file and returns a list of tuples.

    Args:
        path (str): File path

    Raises:
        FileNotFoundError: Raised if the file does not exist
        ValueError: Raised if the data is not in the correct format

    Returns:
        List[Tuple[float, float]]: List of tuples containing milage and price
    """
    # Check if the file exists
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")
    # Read data
    milages = []
    prices = []
    line_count = 1
    with open(path, "r") as file:
        check_header(file, ["km", "price"])
        for line in file:
            line_count += 1
            x, y = line.strip().split(",")
            if x.isnumeric() and y.isnumeric():
                milages.append(float(x))
                prices.append(float(y))
            else:
                raise ValueError(f"Invalid data at line {line_count}: {line}")
    return milages, prices


def save_theta(
    theta0: float,
    theta1: float,
    path: str = THETA_FILE_PATH,
):
    """Save theta0 and theta1 to a CSV file.

    Args:
        path (str): File path
        theta0 (float): New theta0
        theta1 (float): New theta1

    Raises:
        FileNotFoundError: Raised if the directory does not exist
    """
    # Check if the file exists
    if not os.path.exists(os.path.dirname(path)):
        raise FileNotFoundError(f"Directory not found: {path}")
    with open(path, "r") as file:
        check_header(file, ["theta0", "theta1"])
    if IOConstants.THETA_OVERWRITE:
        reset_theta(theta0, theta1)
    else:
        with open(path, "a") as file:
            file.write(f"{theta0},{theta1}\n")


def get_latest_theta(path: str = THETA_FILE_PATH) -> Tuple[float, float]:
    """Get the latest theta0 and theta1 from a CSV file.

    Args:
        path (str): File path

    Raises:
        FileNotFoundError: Raised if the file does not exist
        ValueError: Raised if theta0 and theta1 is empty

    Returns:
        Tuple[float, float]: _description_
    """
    # Check if the file exists
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")
    with open(path, "r") as file:
        check_header(file, ["theta0", "theta1"])
        last_line = None
        for line in file:
            last_line = line
        if last_line is None:
            raise ValueError("theta0 and theta1 is empty")
        thetas = last_line.strip().split(",")
        if len(thetas) != 2:
            raise ValueError("Invalid theta0 and theta1")
        return float(thetas[0]), float(thetas[1])


def reset_theta(theta0: float = 0, theta1: float = 0, path: str = THETA_FILE_PATH):
    """Reset theta0 and theta1 to 0 in a CSV file.

    Args:
        path (str): File path

    Raises:
        FileNotFoundError: Raised if the directory does not exist
    """
    # Check if the file exists
    if not os.path.exists(os.path.dirname(path)):
        raise FileNotFoundError(f"Directory not found: {path}")
    with open(path, "w") as file:
        file.write("theta0,theta1\n")
        file.write(f"{theta0},{theta1}\n")
