import unittest
from src.customer import Customer
class TestCustomer(unittest.TestCase):
    def setUp (self):
        self.customer = Customer("John", 30.00, 25)

    def test_buy_drink(self):
        self.customer.buy_drink(4.00)
        self.assertEqual(26, self.customer.wallet)

    def test_customer_has_age(self):
        self.assertEqual(25, self.customer.age)