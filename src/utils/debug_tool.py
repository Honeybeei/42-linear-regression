from typing import Callable
from utils.string_utils import Color, color_string


def error_catcher(func: Callable, print_success: bool = False) -> Callable:
    """This decorator catches exceptions and prints them in a formatted way.

    Args:
        func (Callable): The function to be decorated.
        print_success (bool, optional): Whether to print a success message when the function completes successfully. Defaults to False.

    Returns:
        Callable: The decorated function.
    """
    function_info = f"{func.__module__}.{func.__name__}"

    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            if print_success:
                print(
                    color_string("Success in ", Color.GREEN)
                    + color_string(f"{function_info}", Color.BLUE)
                )
            return result
        except Exception as e:
            print(
                color_string("An error occurred in ", Color.RED)
                + color_string(f"{function_info}", Color.PURPLE)
                + color_string(f": {e}", Color.RED)
            )
            raise

    return wrapper
