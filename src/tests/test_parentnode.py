import unittest
from leafnode import LeafNode
from parentnode import ParentNode

class TestLeafNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_children(self):
        child1 = LeafNode("span", "One")
        child2 = LeafNode("span", "Two")
        parent = ParentNode("div", [child1, child2])
        result = parent.to_html()
        self.assertEqual(result,
            "<div><span>One</span><span>Two</span></div>")

if __name__ == "__main__":
    unittest.main()
