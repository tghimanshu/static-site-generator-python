from unittest import TestCase
from htmlnode import HTMLNode


class TestHTMLNode(TestCase):
    def test_no_data(self):
        node = HTMLNode()
        self.assertRaises(NotImplementedError, node.to_html)
        self.assertEqual(node.props_to_string(), "")

    def test_with_only_h1_tag(self):
        node = HTMLNode("h1", "Hello World")
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(tag=h1, value=Hello World, children=[], props={})",
        )

    def test_with_only_a_tag(self):
        node = HTMLNode("a", "Hello World", props={"href": "https://boot.dev"})
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(tag=a, value=Hello World, children=[], props={'href': 'https://boot.dev'})",
        )

    def test_with_only_children(self):
        node_child = HTMLNode("b", "Click Me!")
        node = HTMLNode("a", children=[node_child], props={"href": "https://boot.dev"})
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(tag=a, value=None, children=[HTMLNode(tag=b, value=Click Me!, children=[], props={})], props={'href': 'https://boot.dev'})",
        )
