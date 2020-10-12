from typing import Dict, Tuple, List

from good import Good

class Auction:
    __bids: Dict[Good, Dict[int, int]] # good -> person id -> latest bid amount

    def __init__(self, goods):
        self.__bids = {good: {} for good in goods}

    def make_bid(self, person_id: int, good: Good, amount: int):
        self.__bids[good][person_id] = amount

    def get_final_prices(self) -> Dict[Good, int]:
        return {
            good: min(self.__bids[good].values(), default=0)
            for good in self.__bids.keys()
        }

    def get_highest_bid(self, good: Good):
        return max(self.__bids[good].values(), default=1)