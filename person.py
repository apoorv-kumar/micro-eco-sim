from typing import List, Dict

from good import Good
from govt import Govt


class Person:
    __govt: Govt
    __person_id : int
    __current_bids: Dict[Good, int]
    __max_spent_salary: int

    def __init__(self, id, govt):
        self.__govt = govt
        self.__person_id = id
        self.__max_spent_salary = 0
        self.__current_bids = {}

    def make_bids(self) -> bool:  # returns whether any new bids were made
        salary = self.__govt.get_salary(self.__person_id)
        goods = self.__govt.get_goods_list()
        auction = self.__govt.get_auction()
        new_bid_made = False
        for good in goods:
            if auction.get_highest_bid(good) >= self.__current_bids.get(good, 0) and \
                    self.__max_spent_salary < salary:  # keep increasing bids until salary runs out
                self.__max_spent_salary += 1
                self.__current_bids[good] = self.__current_bids.get(good, 0) + 1
                auction.make_bid(self.__person_id, good, self.__current_bids[good])
                new_bid_made = True
        return new_bid_made

    #  at the end of month, give the entire salary to govt
    #  as either savings or payment for goods
    def pay_and_deposit_savings(self):
        self.__current_bids = {}
        self.__max_spent_salary = 0
        self.__govt.receive_payments_and_deposits(self.__person_id)
