import unittest
from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


class TitleSearchTests(unittest.TestCase):
    def test_search_by_title_case_insensitive(self):
        items = [DigitalVideoDisc("The Lion King"), DigitalVideoDisc("Aladdin")]
        self.assertEqual(search_by_title(items, "lion"), [items[0]])
        self.assertEqual(search_by_title(items, "LION"), [items[0]])
        self.assertEqual(search_by_title(items, "missing"), [])
        self.assertEqual(search_by_title([], "lion"), [])
