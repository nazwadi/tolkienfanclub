import unittest

from block_to_block_type import block_to_block_type
from block_to_block_type import BlockType


class TestBlockToBlocks(unittest.TestCase):
    def test_ordered_list(self):
        md = """1. One\n2. Two\n3. Three\n4. Four"""
        self.assertEqual(block_to_block_type(md), BlockType.OLIST)

    def test_unordered_list(self):
        md = """- this\n- that\n- this\n- that"""
        self.assertEqual(block_to_block_type(md), BlockType.ULIST)

    def test_paragraph(self):
        md = """
        This is **bolded** paragraph

        This is another paragraph with _italic_ text and `code` here
        This is the same paragraph on a new line
        """
        block_type = block_to_block_type(md)
        self.assertEqual(BlockType.PARAGRAPH, block_type)

    def test_heading_one(self):
        md = """# Heading One\nTest this"""
        self.assertEqual(block_to_block_type(md), BlockType.HEADING)

    def test_heading_two(self):
        md = """## Heading Two\nTest This"""
        self.assertEqual(block_to_block_type(md), BlockType.HEADING)

    def test_heading_three(self):
        md = """### Heading Three\nTest This"""
        self.assertEqual(block_to_block_type(md), BlockType.HEADING)

    def test_heading_four(self):
        md = """#### Heading Four\nTest This"""
        self.assertEqual(block_to_block_type(md), BlockType.HEADING)

    def test_heading_five(self):
        md = """##### Heading Five\nTest This"""
        self.assertEqual(block_to_block_type(md), BlockType.HEADING)

    def test_heading_six(self):
        md = """###### Heading Six\nTest This"""
        self.assertEqual(block_to_block_type(md), BlockType.HEADING)

    def test_quote(self):
        md = """> This is a quote.
        """
        self.assertEqual(block_to_block_type(md), BlockType.QUOTE)

    def test_code_block(self):
        md = """```int 
        main(void) {
            int value = 0;
            
            return 0;
        }```"""
        self.assertEqual(block_to_block_type(md), BlockType.CODE)
