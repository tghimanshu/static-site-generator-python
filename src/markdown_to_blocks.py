def markdown_to_blocks(markdown):
    return [text.strip() for text in markdown.split("\n\n") if text.strip() != ""]
