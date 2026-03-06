import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_empty(self):
        node = HTMLNode()
        self.assertEqual("", node.props_to_html())
    def test_props_to_html_props(self):
        node = HTMLNode(props={"href": "https://boot.dev"})
        self.assertEqual('href="https://boot.dev"', node.props_to_html())
    def test_props_to_html_props(self):
        node = HTMLNode(props={"href": "https://boot.dev", "target": "_blank"})
        self.assertEqual('href="https://boot.dev" target="_blank"', node.props_to_html())
    def test_to_html(self):
        node = HTMLNode(props={"href": "https://boot.dev"})
        with self.assertRaises(NotImplementedError) as e:
            node.to_html()
        self.assertEqual('not implemented', str(e.exception))

if __name__ == "__main__":
    unittest.main()
