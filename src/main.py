from textnode import TextNode, TextType
from utils import generate_public, generate_page, generate_pages_recursive


def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    generate_public("./static/", "./public/")
    # generate_page("content/index.md", "./template.html", "public/index.html")
    generate_pages_recursive("content/", "./template.html", "public/")
    print(node)


main()
