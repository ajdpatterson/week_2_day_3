import unittest
from src.pub import Pub
from src.customer import *

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100)
        self.customer_1 = Customer("John", 30, 25)
        self.customer_2 = Customer("James", 30, 16)
    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100, self.pub.till)

    def test_pub_has_drinks(self):
        self.assertEqual([], self.pub.drinks)

    def test_pub_sell_drink(self):
        self.pub.sell_drink(4.00, self.customer_1)
        self.assertEqual(104, self.pub.till)
    
    def test_pub_sell_drink__too_young(self):
        self.pub.sell_drink(4.00, self.customer_2)
        self.assertEqual(100, self.pub.till)