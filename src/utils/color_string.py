from enum import Enum


class Color(Enum):
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    BLACK = "\033[30m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"


class ColorString:
    def __init__(self, text: str, color: Color):
        self.text = text
        self.color = color

    def __str__(self):
        return f"{self.color.value}{self.text}{Color.END.value}"
