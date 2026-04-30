from textnode import TextNode, TextType
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        text = old_node.text
        if delimiter not in text:
            new_nodes.append(old_node)
            continue

        if text.count(delimiter) % 2 != 0:
            raise ValueError(
                f"Invalid Markdown: Delimiter '{delimiter}' is not properly closed in text: '{text}'"
            )
        for part in text.split(delimiter):
            if delimiter + part + delimiter in text:
                new_nodes.append(TextNode(part, text_type))
            else:
                new_nodes.append(TextNode(part, TextType.TEXT))
    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)
