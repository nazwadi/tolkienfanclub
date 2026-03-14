from textnode import TextType
from textnode import TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_list = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_list.append(node)
            continue
        new_objects = node.text.split(delimiter)
        if len(new_objects) % 2 == 0:
            raise ValueError("a delimiter was opened but not closed")
        result = []
        for index, item in enumerate(new_objects):
            if not item:
                continue
            else:
                if index % 2 == 0:
                    result.append(TextNode(item, TextType.TEXT))
                else:
                    result.append(TextNode(item, text_type))
        new_list.extend(result)
    return new_list
