class HTMLNode:
    
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("not implemented")

    def props_to_html(self):
        if not self.props:
            return ""
        return ' '.join(f'{k}="{v}"' for k, v in self.props.items())

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props}"


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

    def __repr__(self):
        return f"LeadNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):

    def __init__(self, tag: str, children: list, props: dict = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("no tag found")
        if not self.children:
            raise ValueError("no children found")
        ret = f"<{self.tag}>"
        for node in self.children:
            ret += node.to_html()
        ret += f"</{self.tag}>"
        return ret
