import sys

from textnode import TextNode, TextType
from utils import generate_public, generate_page, generate_pages_recursive


def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    generate_public("./static/", "./docs/")
    # generate_page("content/index.md", "./template.html", "public/index.html")
    generate_pages_recursive(basepath, "content/", "./template.html", "docs/")
    print(node)


main()
