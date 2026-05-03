from textnode import TextNode, TextType
from utils import generate_public


def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    generate_public()
    print(node)


main()
