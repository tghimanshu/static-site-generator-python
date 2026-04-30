from unittest import TestCase
from textnode import TextNode, TextType
from inline_split import (
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_delimiter,
)


class TestInlineSplit(TestCase):
    # Test cases for split_nodes_delimiter function
    def test_no_delimiter(self):
        old_nodes = [TextNode("Hello, world!", TextType.TEXT)]
        self.assertEqual(
            split_nodes_delimiter(old_nodes, "**", TextType.BOLD),
            [TextNode("Hello, world!", TextType.TEXT)],
        )

    def test_bold(self):
        old_nodes = [TextNode("This is **bold** text.", TextType.TEXT)]
        self.assertEqual(
            split_nodes_delimiter(old_nodes, "**", TextType.BOLD),
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" text.", TextType.TEXT),
            ],
        )

    def test_italic(self):
        old_nodes = [TextNode("This is *italic* text.", TextType.TEXT)]
        self.assertEqual(
            split_nodes_delimiter(old_nodes, "*", TextType.ITALIC),
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" text.", TextType.TEXT),
            ],
        )

    def test_multiple_delimiters(self):
        old_nodes = [TextNode("**Bold** and _italic_ text.", TextType.TEXT)]
        self.assertEqual(
            split_nodes_delimiter(old_nodes, "**", TextType.BOLD),
            [
                TextNode("", TextType.TEXT),
                TextNode("Bold", TextType.BOLD),
                TextNode(" and _italic_ text.", TextType.TEXT),
            ],
        )
        self.assertEqual(
            split_nodes_delimiter(old_nodes, "_", TextType.ITALIC),
            [
                TextNode("**Bold** and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" text.", TextType.TEXT),
            ],
        )

    def test_error(self):
        old_nodes = [TextNode("This is **bold text.", TextType.TEXT)]
        with self.assertRaises(ValueError):
            split_nodes_delimiter(old_nodes, "**", TextType.BOLD)

    # Test cases for extract_markdown_images function
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )

        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_multiple(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        matches = extract_markdown_images(text)

        self.assertListEqual(
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
            ],
            matches,
        )

    # Test cases for extract_markdown_links function
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with an [Google](https://www.google.com) link."
        )

        self.assertListEqual([("Google", "https://www.google.com")], matches)

    def test_extract_markdown_links_multiple(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        matches = extract_markdown_links(text)
        self.assertListEqual(
            [
                ("to boot dev", "https://www.boot.dev"),
                ("to youtube", "https://www.youtube.com/@bootdotdev"),
            ],
            matches,
        )

    def test_extract_markdown_links_no_links(self):
        matches = extract_markdown_links("This is text with no links.")
        self.assertListEqual([], matches)
