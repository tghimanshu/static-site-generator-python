from inline_split import text_to_text_nodes
from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type, BlockType
from leafnode import LeafNode
from parentnode import ParentNode
from textnode import TextType


def text_to_children(text):
    text_nodes = text_to_text_nodes(text)

    html_nodes = []
    for text_node in text_nodes:
        if text_node.text_type == TextType.IMAGE:
            html_nodes.append(
                LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
            )
        elif text_node.text_type == TextType.LINK:
            html_nodes.append(LeafNode("a", text_node.text, {"href": text_node.url}))
        elif text_node.text_type == TextType.CODE:
            html_nodes.append(LeafNode("code", text_node.text))
        elif text_node.text_type == TextType.BOLD:
            html_nodes.append(LeafNode("b", text_node.text))
        elif text_node.text_type == TextType.ITALIC:
            html_nodes.append(LeafNode("i", text_node.text))
        else:
            text = text_node.text.replace("\n", " ")
            if text.strip() == "":
                continue
            html_nodes.append(LeafNode("", text_node.text.replace("\n", " ")))

    return html_nodes


def heading_block_to_html_node(block):
    heading_level = 0
    for c in block:
        if c == "#":
            heading_level += 1
        else:
            break
    return LeafNode(f"h{heading_level}", block[heading_level:].strip())


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    childrens = []

    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.HEADING:
            childrens.append(heading_block_to_html_node(block))

        if block_type == BlockType.CODE:
            childrens.append(ParentNode("pre", [LeafNode("code", block[4:-3])]))

        if block_type == BlockType.QUOTE:
            quote_lines = [line[2:].strip() for line in block.split("\n")]
            childrens.append(LeafNode("blockquote", "\n".join(quote_lines)))

        if block_type == BlockType.UNORDERED_LIST:
            list_items = [line[2:].strip() for line in block.split("\n")]
            childrens.append(
                ParentNode(
                    "ul",
                    [ParentNode("li", text_to_children(item)) for item in list_items],
                )
            )

        if block_type == BlockType.ORDERED_LIST:
            list_items = [
                line[line.find(".") + 1 :].strip() for line in block.split("\n")
            ]
            childrens.append(
                ParentNode(
                    "ol",
                    [ParentNode("li", text_to_children(item)) for item in list_items],
                )
            )

        if block_type == BlockType.PARAGRAPH:
            childrens.append(ParentNode("p", children=text_to_children(block)))
    return ParentNode("div", children=childrens)
