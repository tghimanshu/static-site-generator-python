from unittest import TestCase

from extract_title import extract_title


class TestExtractTitle(TestCase):
    def test_extract_title(self):
        self.assertEqual(extract_title("# Hello World"), "Hello World")
        self.assertEqual(extract_title("Wassup\n# Hello World"), "Hello World")

    def test_extract_title_no_title(self):
        self.assertRaises(ValueError, extract_title, "Wassup\nHello World")
