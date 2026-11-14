import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


class TestSearch(unittest.TestCase):
    def setUp(self):
        self.dvds = [
            DigitalVideoDisc("The Lion King"),
            DigitalVideoDisc("Star Wars"),
            DigitalVideoDisc("Aladdin"),
        ]

    def test_search_case_insensitive(self):
        result = search_by_title(self.dvds, "lion")
        self.assertEqual([dvd.title for dvd in result], ["The Lion King"])

    def test_search_unmatched_title(self):
        self.assertEqual(search_by_title(self.dvds, "Avatar"), [])

    def test_empty_keyword_returns_copy(self):
        result = search_by_title(self.dvds, "")
        self.assertEqual(result, self.dvds)
        self.assertIsNot(result, self.dvds)

    def test_non_string_keyword_is_invalid(self):
        with self.assertRaises(TypeError):
            search_by_title(self.dvds, None)


if __name__ == "__main__":
    unittest.main()
