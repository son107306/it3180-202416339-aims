import unittest
from aims.cart import create_cart

class TestCart(unittest.TestCase):
    def test_create_cart(self):
        cart = create_cart()
        self.assertEqual(cart, [])
