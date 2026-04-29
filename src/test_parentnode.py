from unittest import TestCase

from leafnode import LeafNode
from parentnode import ParentNode


class TestParentNode(TestCase):
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

    def test_to_html_no_tag(self):
        child_node = LeafNode("b", "child")
        parent_node = ParentNode("", [child_node])
        self.assertRaises(ValueError, parent_node.to_html)

    def test_to_html_no_children(self):
        parent_node = ParentNode("a", [])
        self.assertRaises(ValueError, parent_node.to_html)

    def test_to_html_no_tag_and_children(self):
        parent_node = ParentNode("", [])
        self.assertRaises(ValueError, parent_node.to_html)
