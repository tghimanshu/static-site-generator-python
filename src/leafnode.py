from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.tag == "img":
            if "src" not in self.props:
                raise ValueError("Image tag must have a src property")
            return f"<{self.tag}{self.props_to_string()} />"

        if not self.value:
            raise ValueError("LeafNode must have a value")

        if self.tag is None:
            return self.value
        if self.tag == "":
            return self.value

        return f"<{self.tag}{self.props_to_string()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, props={self.props})"
