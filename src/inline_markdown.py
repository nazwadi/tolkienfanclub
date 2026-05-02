from textnode import TextType
from textnode import TextNode
from extract_links import extract_markdown_links, extract_markdown_images

def split_nodes_image(old_nodes):
    new_list = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_list.append(node)
            continue
        images = extract_markdown_images(node.text)
        if not images:
            new_list.append(node)
            continue
        result = []
        remaining_text = node.text
        for alt, url in images:
            sections = remaining_text.split(f"![{alt}]({url})", 1)
            if sections[0] != "":
                result.append(TextNode(sections[0], TextType.TEXT))
            result.append(TextNode(alt, TextType.IMAGE, url))
            remaining_text = sections[1]
        if remaining_text != "":
            result.append(TextNode(remaining_text, TextType.TEXT))
        new_list.extend(result)
    return new_list

def split_nodes_link(old_nodes):
    new_list = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_list.append(node)
            continue
        links = extract_markdown_links(node.text)
        if not links:
            new_list.append(node)
            continue
        result = []
        remaining_text = node.text
        for alt, url in links:
            sections = remaining_text.split(f"[{alt}]({url})", 1)
            if sections[0] != "":
                result.append(TextNode(sections[0], TextType.TEXT))
            result.append(TextNode(alt, TextType.LINK, url))
            remaining_text = sections[1]
        if remaining_text != "":
            result.append(TextNode(remaining_text, TextType.TEXT))
        new_list.extend(result)
    return new_list

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
