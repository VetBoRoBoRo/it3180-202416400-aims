import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class SortTests(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.cart.items = [DigitalVideoDisc("Zebra", cost=5), DigitalVideoDisc("apple", cost=10)]

    def test_sort_by_title(self):
        self.cart.sort_by_title()
        self.assertEqual([dvd.title for dvd in self.cart.items], ["apple", "Zebra"])

    def test_sort_by_cost(self):
        self.cart.sort_by_cost()
        self.assertEqual([dvd.cost for dvd in self.cart.items], [5, 10])
