from textnode import TextNode, TextType
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        text = old_node.text
        if text == "":
            continue

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
    return re.findall(r"(?<!\!)\[(.*?)\]\((.*?)\)", text)


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        text = old_node.text
        images = extract_markdown_images(text)

        if not images or len(images) == 0:
            new_nodes.append(old_node)
            continue

        for alt_text, url in images:
            extract = text.split(f"![{alt_text}]({url})")
            left = extract[0]
            if left != "":
                new_nodes.append(TextNode(left, TextType.TEXT))
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
            # if len(extract) > 1:
            text = extract[1]

        right = text.split(f"![{images[-1][0]}]({images[-1][1]})")[-1]
        if right != "":
            new_nodes.append(TextNode(right, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        text = old_node.text
        links = extract_markdown_links(text)

        if not links or len(links) == 0:
            new_nodes.append(old_node)
            continue

        for alt_text, url in links:
            extract = text.split(f"[{alt_text}]({url})")
            left = extract[0]
            if left != "":
                new_nodes.append(TextNode(left, TextType.TEXT))
            new_nodes.append(TextNode(alt_text, TextType.LINK, url))
            # if len(extract) > 1:
            text = extract[1]

        right = text.split(f"[{links[-1][0]}]({links[-1][1]})")[-1]
        if right != "":
            new_nodes.append(TextNode(right, TextType.TEXT))
    return new_nodes


def text_to_text_nodes(text):
    new_nodes = split_nodes_delimiter(
        [TextNode(text, TextType.TEXT)], "**", TextType.BOLD
    )
    new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)

    return new_nodes
