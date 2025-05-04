import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        output = HTMLNode("tag", "value", "children", "{'href': 'https://www.google.com','target': '_blank'}")
        output.props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        output_expected = " href='https://www.google.com' target='_blank'"
        self.assertEqual(output.props_to_html(), output_expected)

if __name__ == "__main__":
    unittest.main()
