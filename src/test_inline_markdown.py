import unittest

from inline_markdown import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

class TestSplitImages(unittest.TestCase):
    def test_split_image_no_images(self):
        node = TextNode("Just plain text", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([node], new_nodes)

class TestSplitLinks(unittest.TestCase):
    def test_split_link_no_links(self):
        node = TextNode("Just plain text", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([node], new_nodes)
