from typing import List, Optional

from good import Good
from govt import Govt
from person import Person


class Universe:
    __govt: Govt
    __people: List[Person]

    def __init__(self):
        starting_goods = ['sugar', 'rice', 'oil']
        person_id_to_starting_salaries = {
            1: 100,
            2: 150,
            3: 175,
            4: 300
        }
        self.__govt = Govt(person_id_to_starting_salaries, starting_goods)
        self.__people = [
            Person(person_id, self.__govt)
            for person_id in person_id_to_starting_salaries.keys()
        ]

    def run_month(self, add_good: Optional[Good] = None,
                  increase_salary_percent: Optional[int] = None
                  ):
        print("\nNEW MONTH:")
        if add_good:
            print(f"Adding new good: {add_good}")
            self.__govt.add_new_good(add_good)
        if increase_salary_percent:
            print(f"Increasing salaries by: {increase_salary_percent}%")
            self.__govt.increase_salary(increase_salary_percent)

        self.__govt.new_month()
        # people bid until no new bids
        bids = [True]
        while any(bids):
            bids = [
                person.make_bids() for person in self.__people
            ]
        # people make final payments and save remaining
        for person in self.__people:
            person.pay_and_deposit_savings()

        self.__govt.report_prices()
        self.__govt.report_savings()
        self.__govt.report_inflation()
