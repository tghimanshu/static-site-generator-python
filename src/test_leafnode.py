from leafnode import LeafNode
from unittest import TestCase


class TestLeafNode(TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", props={"href": "https://google.com"})
        self.assertEqual(node.to_html(), '<a href="https://google.com">Click me!</a>')

    def test_leaf_to_html_a_with_no_value(self):
        node = LeafNode("a", "", props={"href": "https://google.com"})
        self.assertRaises(ValueError, node.to_html)

    def test_leaf_to_html_a_repr(self):
        node = LeafNode("a", "", props={"href": "https://google.com"})
        self.assertRaises(ValueError, node.to_html)
