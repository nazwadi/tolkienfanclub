from htmlnode import HTMLNode

class LeafNode(HTMLNode):

    def __init__(self, tag, value, children=None, props=None):
        super().__init__(tag, value, children, props)

    def __init_subclass__(cls, **kwargs):
        raise TypeError(f"Cannot subclass {cls.__name__!r} - it is a final class")

    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value.")
        if not self.tag:
            return f"{self.value}" # return value as raw text
        return f"<{self.tag}>{self.value}</{self.tag}>"
