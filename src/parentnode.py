from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode must have a tag")

        if not self.children or self.children == []:
            raise ValueError("ParentNode must have children(s)")

        children_html = "".join(child.to_html() for child in self.children)
        return f"<{self.tag}{self.props_to_string()}>{children_html}</{self.tag}>"
