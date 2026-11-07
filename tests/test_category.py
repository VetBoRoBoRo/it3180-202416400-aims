import unittest
from aims.dvd import DigitalVideoDisc
from aims.search import search_by_category


class SearchTests(unittest.TestCase):
    def test_search_by_category(self):
        items = [DigitalVideoDisc("Lion King", "Animation"), DigitalVideoDisc("Star Wars", "Sci-Fi")]
        self.assertEqual(search_by_category(items, "animation"), [items[0]])
        self.assertEqual(search_by_category(items, "Drama"), [])
