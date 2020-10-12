from typing import List, Dict

from auction import Auction
from good import Good


class Govt:
    __current_auction: Auction
    __historical_auction_prices: List[Dict[Good, int]]
    __goods: List[Good]
    __bank: Dict[int, int]  # person id -> savings amount
    __salaries: Dict[int, int]  # person id -> salary amount

    def __init__(self, salaries: Dict[int, int], goods: List[Good]):
        self.__historical_auction_prices = []
        self.__salaries = salaries
        self.__goods = goods
        self.__current_auction = None
        self.__bank = {}

    def get_salary(self, person_id: int):
        return self.__salaries[person_id]

    def get_goods_list(self):
        return self.__goods

    def get_auction(self):
        return self.__current_auction

    def new_month(self):
        if self.__current_auction:
            self.__historical_auction_prices.append(self.__current_auction.get_final_prices())
        self.__current_auction = Auction(self.__goods)

    def increase_salary(self, percent):
        self.__salaries = {
            person_id: round(salary*(1+(percent/100)))
            for person_id, salary in self.__salaries.items()
        }

    def add_new_good(self, good: Good):
        self.__goods.append(good)

    def receive_payments_and_deposits(self, person_id):
        good_prices = self.__current_auction.get_final_prices()
        total_expenditure = sum(good_prices.values())
        savings = self.__salaries[person_id] - total_expenditure
        self.__bank[person_id] = self.__bank.setdefault(person_id, 0) + savings

    def report_prices(self):
        prices = self.__current_auction.get_final_prices()
        print("PRICES:")
        for good in self.__goods:
            print(f"\t{good} - Rs {prices[good]}")

    def report_inflation(self):
        if len(self.__historical_auction_prices) > 0:
            print("INFLATION NUMBERS:")
            for good in self.__goods:
                prev_price = self.__historical_auction_prices[-1].get(good)
                latest_price = self.__current_auction.get_final_prices()[good]
                if prev_price:
                    inflation = round((latest_price - prev_price)*100/prev_price, 2)
                else:
                    inflation = "NA"
                print(f"\t{good} - {inflation}%")

    def report_savings(self):
        print("SAVINGS")
        for person, saving in self.__bank.items():
            print(f"\tPerson {person}: Rs {saving}")
