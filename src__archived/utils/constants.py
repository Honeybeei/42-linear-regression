from dataclasses import dataclass


@dataclass(frozen=True)
class IOConstants:
    THETA_OVERWRITE: bool = True
    DATA_DIR: str = "data"
    DATA_FILE: str = "data.csv"
    THETA_FILE: str = "theta.csv"
