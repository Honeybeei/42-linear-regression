from typing import Final
import os

# Define the path to the data file
DATA_FILE_LOCATION: Final[str] = os.path.join(
    os.path.dirname(__file__), "..", "..", "data"
)
DATA_FILE_PATH: Final[str] = os.path.join(DATA_FILE_LOCATION, "data.csv")
THETA_FILE_PATH: Final[str] = os.path.join(DATA_FILE_LOCATION, "theta.csv")
