from dataclasses import dataclass


@dataclass(frozen=True)
class CoreConstants:
    INITIAL_LEARNING_RATE: float = 1.6e-10
    LEARNING_RATE_DECREASE_FACTOR: float = 0.99999
    # ITERATIONS: int = 8  # when not using theta0 acceleration
    ITERATIONS: int = 10000  # when using theta0 acceleration
    ITERATION_PRINT_INTERVAL: int = 1000

    # STARTING_TYPE: str = "optimized"
    STARTING_TYPE: str = "random"
    # STARTING_TYPE: str = "zero"

    RANDOM_THETA0_MIN: int = 6000
    RANDOM_THETA0_MAX: int = 10000
    RANDOM_THETA1_MIN: float = -1
    RANDOM_THETA1_MAX: float = 1
    # COST_DIFF_THRESHOLD = 0.0002  # when not using theta0 acceleration
    COST_DIFF_THRESHOLD = 0.000005

    USE_THETA0_ACCELERATION: bool = True
    # USE_THETA0_ACCELERATION: bool = False
    THETA0_ACCELERATION_RATE: int = 100000
