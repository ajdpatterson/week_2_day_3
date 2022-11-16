from src.customer import *

class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def increase_till(self, amount):
        self.till += amount

    def sell_drink(self, drink_cost, customer):
        if customer.age >= 18:
            self.increase_till(drink_cost)
            customer.buy_drink(drink_cost)