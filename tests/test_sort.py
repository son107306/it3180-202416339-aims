import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestSort(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.cart.add_dvd(DigitalVideoDisc("Zulu", cost=10))
        self.cart.add_dvd(DigitalVideoDisc("alpha", cost=20))
        self.cart.add_dvd(DigitalVideoDisc("Alpha", cost=15))

    def test_sort_by_title_then_cost(self):
        self.cart.sort_by_title()
        self.assertEqual(
            [(dvd.title, dvd.cost) for dvd in self.cart.items],
            [("alpha", 20), ("Alpha", 15), ("Zulu", 10)],
        )

    def test_sort_by_cost_descending(self):
        self.cart.sort_by_cost()
        self.assertEqual([dvd.cost for dvd in self.cart.items], [20, 15, 10])


if __name__ == "__main__":
    unittest.main()
