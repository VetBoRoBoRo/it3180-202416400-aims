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


if __name__ == "__main__":
    unittest.main()
