from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(markdown):
    if re.match(r"^#{1,6} ", markdown):
        return BlockType.HEADING

    if re.match(r"^```((.|\n)*)```$", markdown):
        return BlockType.CODE

    lines = markdown.splitlines()
    if all(re.match(r"^>", line) for line in lines):
        return BlockType.QUOTE
    if all(re.match(r"^[-*] ", line) for line in lines):
        return BlockType.UNORDERED_LIST
    if all(re.match(r"^\d+\. ", line) for line in lines):
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
