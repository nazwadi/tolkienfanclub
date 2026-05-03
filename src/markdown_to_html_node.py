from markdown_blocks import block_to_block_type, BlockType
from htmlnode import ParentNode
from markdown_blocks import markdown_to_blocks

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                node = ParentNode(value="paragraph")
                pass
            case BlockType.HEADING:
                pass
            case BlockType.QUOTE:
                pass
            case BlockType.CODE:
                pass
            case BlockType.OLIST:
                pass
            case BlockType.ULIST:
                pass
            case _:
                pass