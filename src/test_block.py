import unittest
from block import BlockType, block_to_block_type

class TestBlock(unittest.TestCase):
    def block_to_block_type_heading(self):
        result = (block_to_block_type("# heading"))
        self.assertEqual(BlockType.HEADING, result)

        result = (block_to_block_type("# #heading"))
        self.assertEqual(BlockType.HEADING, result)

        result = (block_to_block_type("###### heading"))
        self.assertEqual(BlockType.HEADING, result)

        result = (block_to_block_type("####### notheading"))
        self.assertEqual(BlockType.PARAGRAPH, result)

        result = (block_to_block_type("#######notheading"))
        self.assertEqual(BlockType.PARAGRAPH, result)

    def block_to_block_type_quote(self):
        result = (block_to_block_type("> quote"))
        self.assertEqual(BlockType.QUOTE, result)

        result = (block_to_block_type("#heading"))
        self.assertNotEqual(BlockType.QUOTE, result)

        result = (block_to_block_type(">quote"))
        self.assertEqual(BlockType.QUOTE, result)

    def block_to_block_type_paragraph(self):
        result = (block_to_block_type(" quote"))
        self.assertEqual(BlockType.PARAGRAPH, result)

        result = (block_to_block_type("####### para"))
        self.assertEqual(BlockType.PARAGRAPH, result)

        result = (block_to_block_type("dbadgapdgapdpagdgapdg"))
        self.assertEqual(BlockType.PARAGRAPH, result)

    def block_to_block_type_code(self):
        result = (block_to_block_type("```ǹot code"))
        self.assertNotEqual(BlockType.CODE, result)

        result = (block_to_block_type("#```code```"))
        self.assertEqual(BlockType.CODE, result)

    def block_to_block_type_ordered_list(self):
        result = (block_to_block_type("1.notlist"))
        self.assertNotEqual(BlockType.ORDERED_LIST, result)
        result = (block_to_block_type("1. notlist\n2.not"))
        self.assertNotEqual(BlockType.ORDERED_LIST, result)
        result = (block_to_block_type("1. notlist\n 3. yes"))
        self.assertNotEqual(BlockType.ORDERED_LIST, result)

        result = (block_to_block_type("1. list"))
        self.assertEqual(BlockType.ORDERED_LIST, result)
        result = (block_to_block_type("1. list\n 2. yes"))
        self.assertEqual(BlockType.ORDERED_LIST, result)

    def block_to_block_type_list(self):
        result = (block_to_block_type("-notlist"))
        self.assertNotEqual(BlockType.ORDERED_LIST, result)
        result = (block_to_block_type("- notlist\n-notlist"))
        self.assertNotEqual(BlockType.ORDERED_LIST, result)

        result = (block_to_block_type("- list"))
        self.assertEqual(BlockType.ORDERED_LIST, result)
        result = (block_to_block_type("- list\n - cont"))
        self.assertEqual(BlockType.ORDERED_LIST, result)

if __name__ == "__main__":
    unittest.main()
