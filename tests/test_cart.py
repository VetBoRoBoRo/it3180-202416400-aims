import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class CartTests(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        for i in range(20):
            self.assertTrue(cart.add_dvd(DigitalVideoDisc(str(i))))
        self.assertFalse(cart.add_dvd(DigitalVideoDisc("21st")))
        self.assertEqual(len(cart.items), 20)

    def test_discounted_total(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("Example", cost=100))
        self.assertEqual(cart.total_cost_with_discount(20), 80)

    def test_discount_rejects_invalid_percent(self):
        with self.assertRaises(ValueError):
            Cart().total_cost_with_discount(150)

    def test_total_cost(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("A", cost=19.95))
        cart.add_dvd(DigitalVideoDisc("B", cost=24.95))
        cart.add_dvd(DigitalVideoDisc("C", cost=18.99))
        self.assertEqual(cart.total_cost(), 63.89)


if __name__ == "__main__":
    unittest.main()
