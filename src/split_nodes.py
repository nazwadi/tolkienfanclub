from textnode import TextType
from textnode import TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_list = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_list.append(node)
            continue
        new_objects = node.text.split(delimiter)
        return [
            TextNode(new_objects[0], TextType.TEXT),
            TextNode(new_objects[1], TextType.TEXT)
        ]

