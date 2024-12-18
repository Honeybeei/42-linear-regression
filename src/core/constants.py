from dataclasses import dataclass


@dataclass(frozen=True)
class CoreConstants:
    INITIAL_LEARNING_RATE: float = 1.6e-10
    LEARNING_RATE_DECREASE_FACTOR: float = 0.99999
    ITERATIONS: int = 10
    ITERATION_PRINT_INTERVAL: int = 100
    OPTIMIZED_START = True
    COST_DIFF_THRESHOLD = 0.0002
