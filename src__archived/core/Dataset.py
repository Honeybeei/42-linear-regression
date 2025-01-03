from typing import List
from utils.string_utils import color_string, Color


class Dataset:
    def __init__(self, milages: List[float] = None, prices: List[float] = None):
        self.dataset = []
        if milages is not None and prices is not None:
            self.add_data(milages, prices)

    def get_milages(self) -> List[float]:
        return [x[0] for x in self.dataset]

    def get_prices(self) -> List[float]:
        return [x[1] for x in self.dataset]

    def get_milage(self, index: int) -> float:
        return self.dataset[index][0]

    def get_price(self, index: int) -> float:
        return self.dataset[index][1]

    def get_size(self) -> int:
        return len(self.dataset)

    def add_data(self, milages: List[float], prices: List[float]):
        # check if the data is valid
        if len(milages) != len(prices):
            raise ValueError("Milages and prices must have the same length")
        self.dataset += [(milages[i], prices[i]) for i in range(len(milages))]

    def print_data(self):
        print(color_string("\nDataset:", Color.BLUE))
        MAX_WIDTH = 61
        print("-" * MAX_WIDTH)
        # print the header (center aligned)
        print(f"|{'Milage':^29}|{'Price':^29}|")
        print("-" * MAX_WIDTH)
        # print the data
        for milage, price in self.dataset:
            print(f"|{milage:>29.2f}|{price:>29.2f}|")
        print("-" * MAX_WIDTH)
