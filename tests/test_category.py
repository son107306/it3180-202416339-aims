import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_category


class TestSearchByCategory(unittest.TestCase):
    def setUp(self):
        self.dvds = [
            DigitalVideoDisc("The Lion King", category="Animation"),
            DigitalVideoDisc("Aladdin", category="Animation"),
            DigitalVideoDisc("Star Wars", category="Science Fiction"),
        ]

    def test_case_insensitive_category(self):
        result = search_by_category(self.dvds, "animation")
        self.assertEqual([disc.title for disc in result], ["The Lion King", "Aladdin"])

    def test_nonexistent_category(self):
        self.assertEqual(search_by_category(self.dvds, "Romance"), [])

    def test_empty_category_returns_copy(self):
        result = search_by_category(self.dvds, "")
        self.assertEqual(result, self.dvds)
        self.assertIsNot(result, self.dvds)

    def test_invalid_category(self):
        with self.assertRaises(TypeError):
            search_by_category(self.dvds, None)


if __name__ == "__main__":
    unittest.main()
