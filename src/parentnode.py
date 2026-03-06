from htmlnode import HTMLNode

class ParentNode(HTMLNode):

    def __init__(self,
                 tag: str,
                 children: list,
                 props: dict = None):
        self.tag = tag
        self.children = children
        self.props = props

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
