import unittest
from listutil import unique
 
class ListUtilTest(unittest.TestCase):
 
    def test_one_item_list(self):
        self.assertListEqual( ['hi'], unique(['hi']))
        self.assertListEqual([0], unique([0]))
        self.assertEqual([[]],unique([[]]))

    def test_empty_list(self):
        self.assertEqual([], unique([]))

if __name__ == '__main__':
    unittest.main()