import unittest

from aims.cart import Cart, MAX_NUMBERS_ORDERED, create_cart
from aims.dvd import DigitalVideoDisc


class TestCart(unittest.TestCase):
    def test_original_create_cart_helper(self):
        self.assertEqual(create_cart(), [])

    def test_add_and_remove_dvd(self):
        cart = Cart()
        disc = DigitalVideoDisc("Example", cost=5)
        self.assertTrue(cart.add_dvd(disc))
        self.assertTrue(cart.remove_dvd(disc))
        self.assertFalse(cart.remove_dvd(disc))

    def test_total_cost_matches_lab_demo(self):
        cart = Cart()
        for title, price in [("Lion", 19.95), ("Wars", 24.95), ("Aladdin", 18.99)]:
            cart.add_dvd(DigitalVideoDisc(title, cost=price))
        self.assertAlmostEqual(cart.total_cost(), 63.89)

    def test_reject_twenty_first_dvd(self):
        cart = Cart()
        for i in range(MAX_NUMBERS_ORDERED):
            self.assertTrue(cart.add_dvd(DigitalVideoDisc(f"DVD {i}", cost=1)))
        self.assertFalse(cart.add_dvd(DigitalVideoDisc("DVD 21", cost=1)))
        self.assertEqual(len(cart.items), MAX_NUMBERS_ORDERED)


if __name__ == "__main__":
    unittest.main()
