from typing import List, Tuple
import os
from constants.path import DATA_FILE_PATH, THETA_FILE_PATH
from constants.config import APPEND_THETA_DATA


def _read_last_line_from_file(path: str) -> str:
    with open(path, "r") as file:
        lines = file.readlines()
        return lines[-1].strip()


def _read_first_line_from_file(path: str) -> str:
    with open(path, "r") as file:
        return file.readline().strip()


def _save_data_to_csv(data: List[Tuple[float, ...]], path: str, append: bool):
    header = _read_first_line_from_file(path)
    col_count = len(header.split(","))
    if append:
        with open(path, "a") as file:
            for row in data:
                if len(row) != col_count:
                    raise ValueError(
                        f"Row {row} has {len(row)} columns, expected {col_count}"
                    )
                file.write(",".join(map(str, row)) + "\n")
    else:
        with open(path, "w") as file:
            file.write(header + "\n")
            for row in data:
                if len(row) != col_count:
                    raise ValueError(
                        f"Row {row} has {len(row)} columns, expected {col_count}"
                    )
                file.write(",".join(map(str, row)) + "\n")


def check_file_existence(path: str):
    if not os.path.exists(path):
        raise FileNotFoundError(f"{path} does not exist.")


def get_theta_from_csv(path: str = THETA_FILE_PATH) -> Tuple[float, float]:
    line = _read_last_line_from_file(path)
    return tuple(map(float, line.split(",")))


def save_theta_to_csv(
    theta: Tuple[float, float],
    path: str = THETA_FILE_PATH,
    append: bool = APPEND_THETA_DATA,
):
    _save_data_to_csv([theta], path, append)


def get_data_from_csv(path: str = DATA_FILE_PATH) -> List[Tuple[float, ...]]:
    """
    Reads data from a CSV file and returns it as a list of tuples.

    Returns:
        List[Tuple[float, ...]]: A list of tuples where each tuple represents a row of data from the CSV file.
    """
    data = []
    row_index = 0

    with open(path, "r") as file:
        # read header and check column count
        col_count = len(file.readline().strip().split(","))
        row_index += 1

        # read data
        for line in file:
            row = line.strip().split(",")
            if len(row) != col_count:
                raise ValueError(
                    f"Row {row_index} has {len(row)} columns, expected {col_count}"
                )
            data.append(tuple(map(float, row)))
            row_index += 1
    return data
