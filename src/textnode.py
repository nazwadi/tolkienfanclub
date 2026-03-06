from enum import Enum
from htmlnode import HTMLNode
from leafnode import LeafNode


class TextType(Enum):
    BOLD = "bold"
    ITALIC = "italic"
    LINK = "link"
    TEXT = "text"
    URL = "url"
    CODE = "code"
    IMAGE = "image"

class TextNode():

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        return (self.text == other.text and 
                self.text_type == other.text_type and 
                self.url == other.url)

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(tag=None, value=text_node.text)
        case TextType.BOLD:
            return LeafNode(tag="b", value=text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag="i", value=text_node.text)
        case TextType.CODE:
            return LeafNode(tag="code", value=text_node.text)
        case TextType.LINK:
            props = {"href": text_node.url}
            return LeafNode(tag="a", props=props,value=text_node.text)
        case TextType.IMAGE:
            props={"src" : text_node.url, "alt" : text_node.text}
            return LeafNode(tag="img", value="", props=props)
        case _:
            raise ValueError(f"invalid text type: {text_node.text_type}")

