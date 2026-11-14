import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestDiscount(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.cart.add_dvd(DigitalVideoDisc("Sample", cost=100.0))

    def test_twenty_percent_discount(self):
        self.assertAlmostEqual(self.cart.total_cost_with_discount(20), 80)

    def test_no_discount(self):
        self.assertAlmostEqual(self.cart.total_cost_with_discount(0), 100)

    def test_invalid_percent(self):
        for percent in (-1, 101):
            with self.subTest(percent=percent):
                with self.assertRaises(ValueError):
                    self.cart.total_cost_with_discount(percent)


if __name__ == "__main__":
    unittest.main()
