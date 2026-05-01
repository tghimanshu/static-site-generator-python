from unittest import TestCase
from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import BlockType, block_to_block_type


class TestBlockToBlockType(TestCase):
    def test_basic_blocks(self):
        text = """
# Heading 1 block:

```
def hello_world():
    print("Hello, world!")
```

> This is a quote block.

- Unordered list item 1
- Unordered list item 2

1. Ordered list item 1
2. Ordered list item 2

This is a paragraph block.
"""
        blocks = markdown_to_blocks(text)
        block_types = []
        for block in blocks:
            block_types.append(block_to_block_type(block))

        self.assertEqual(
            block_types,
            [
                BlockType.HEADING,
                BlockType.CODE,
                BlockType.QUOTE,
                BlockType.UNORDERED_LIST,
                BlockType.ORDERED_LIST,
                BlockType.PARAGRAPH,
            ],
        )

    def test_heading_blocks(self):
        text = """
# Heading 1 block:

## Heading 2 block:

### Heading 3 block:

#### Heading 4 block:

##### Heading 5 block:

###### Heading 6 block:
"""
        blocks = markdown_to_blocks(text)
        block_types = []
        for block in blocks:
            block_types.append(block_to_block_type(block))

        self.assertEqual(
            block_types,
            [
                BlockType.HEADING,
                BlockType.HEADING,
                BlockType.HEADING,
                BlockType.HEADING,
                BlockType.HEADING,
                BlockType.HEADING,
            ],
        )

    def test_quote_blocks(self):
        text = """
> this is a quote
> this is a continued quote
"""
        blocks = markdown_to_blocks(text)
        block_types = []
        for block in blocks:
            block_types.append(block_to_block_type(block))

        self.assertEqual(
            block_types,
            [BlockType.QUOTE],
        )

    def test_unordered_blocks(self):
        text = """
- this is a quote
- this is a continued quote
"""
        blocks = markdown_to_blocks(text)
        block_types = []
        for block in blocks:
            block_types.append(block_to_block_type(block))

        self.assertEqual(
            block_types,
            [BlockType.UNORDERED_LIST],
        )

    def test_ordered_blocks(self):
        text = """
1. this is a quote
2. this is a continued quote
"""
        blocks = markdown_to_blocks(text)
        block_types = []
        for block in blocks:
            block_types.append(block_to_block_type(block))

        self.assertEqual(
            block_types,
            [BlockType.ORDERED_LIST],
        )
