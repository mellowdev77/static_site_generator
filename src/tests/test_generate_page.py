import unittest
from generate_page import *

class TestGeneratePage(unittest.TestCase):
    def test_extract_title(self):

        output = extract_title("# Helloooo")
        output_expected = "Helloooo"
        self.assertEqual(output, output_expected)

        output = extract_title("#Helloooo")
        output_expected = "Helloooo"
        self.assertEqual(output, output_expected)

        output = extract_title("## Helloooo")
        output_expected = "Helloooo"
        self.assertEqual(output, output_expected)
