from time import sleep
import os
import platform
from utils import color_string, Color


def display_exit_countdown(seconds: int = 3):
    for i in range(seconds, 0, -1):
        print(f"Exiting in {i}...", end="\r")
        sleep(1)
    clear_terminal()


def clear_terminal():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def press_any_key():
    input(
        color_string(
            "\nPress Enter to continue...",
            Color.UNDERLINE,
        ),
    )
