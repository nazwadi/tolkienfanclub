import unittest
from utils import extract_title


class MyTestCase(unittest.TestCase):
    def test_extract_title_hello(self):
        md = "# Hello, World!"
        title = extract_title(md)
        self.assertEqual("Hello, World!", title)  # add assertion here

    def test_extract_title_fail(self):
        md = "# Hello, World"
        title = extract_title(md)
        self.assertNotEqual("Hello, World!", title)  # add assertion here

    def test_extract_title_subheader(self):
        md = "# Hello, World!\n\n## Not the title"
        title = extract_title(md)
        self.assertEqual("Hello, World!", title)  # add assertion here


if __name__ == '__main__':
    unittest.main()
