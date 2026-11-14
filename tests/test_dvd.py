import unittest

from aims.dvd import DVD, DigitalVideoDisc


class TestDVD(unittest.TestCase):
    def test_default_properties_and_compatibility_alias(self):
        disc = DVD("Example")
        self.assertIsInstance(disc, DigitalVideoDisc)
        self.assertEqual(disc.category, "")
        self.assertEqual(disc.cost, 0.0)

    def test_reject_invalid_price(self):
        with self.assertRaises(ValueError):
            DigitalVideoDisc("Invalid", cost=-1)


if __name__ == "__main__":
    unittest.main()
