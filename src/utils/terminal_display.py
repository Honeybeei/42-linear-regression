from .color_string import Color, ColorString
import os
import platform
from typing import List


def clear_terminal():
    """Clears the terminal screen."""
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def press_any_key(
    prompt: str = "Press Enter to continue...",
    string_style: Color = Color.BOLD,
):
    """Prompts the user to press Enter to continue."""
    input(
        ColorString(
            f"\n{prompt}\n",
            string_style,
        )
    )


def ask_yes_no_question(
    question: str,
    string_style: Color = Color.BOLD,
    error_message_style: Color = Color.RED,
    strict: bool = False,
    max_attempts: int = 5,
) -> bool:
    """Asks the user a yes/no question. If the user inputs 'y', returns True; otherwise, returns False."""
    print(ColorString(question, string_style))
    for attempt in range(max_attempts):
        answer = input(ColorString("Please enter 'y' or 'n': ", string_style))
        if not strict:
            return answer.lower() == "y"
        else:
            if answer == "y":
                return True
            elif answer == "n":
                return False
            elif strict:
                print(
                    ColorString(
                        f"Invalid input [{attempt + 1}/{max_attempts}]",
                        error_message_style,
                    ),
                )
    raise ValueError("Too many invalid inputs.")


def display_menu(
    menu: List[str],
    title: str = "Menu Title",
    max_attempts: int = 5,
) -> str:
    """Displays a menu to the user and returns the user's selection."""
    print("\n", ColorString(title, Color.BOLD), "\n")
    menu_length = len(menu)
    menu_length_digits = len(str(menu_length))

    # Display the menu options
    for i in range(menu_length):
        print(
            ColorString(
                f"[{i + 1:0{menu_length_digits}}] {menu[i]}",
                Color.CYAN,
            )
        )

    # Loop until the user enters a valid selection
    for attempt in range(max_attempts):

        user_input = input("\nPlease enter your selection: ")
        if user_input.isdigit():
            user_input = int(user_input)
            if 1 <= user_input <= menu_length:
                return menu[user_input - 1]
        print(
            ColorString(
                f"Invalid input. Please try again [{attempt + 1}/{max_attempts}]",
                Color.RED,
            )
        )
    raise ValueError("Too many invalid inputs.")
