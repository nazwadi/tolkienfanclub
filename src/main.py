from textnode import TextNode, TextType
from utils import generate_public, generate_page


def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    generate_public("./static/", "./public/")
    generate_page("content/index.md", "./template.html", "public/index.html")
    print(node)


main()
