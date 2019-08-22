import unittest
from listutil import unique
 
class ListUtilTest(unittest.TestCase):
 
    def test_one_item_list(self):
        self.assertListEqual(['hi'], unique(['hi']))
        self.assertListEqual([0], unique([0]))
        self.assertEqual([5.54], unique([5.54]))
        self.assertEqual([[]], unique([[]]))

    def test_same_item_many_times_list(self):
        self.assertEqual(['cat'], unique(['cat', 'cat', 'cat', 'cat']))
        self.assertEqual([100], unique([100, 100, 100]))
        self.assertEqual([20.867], unique([20.867, 20.867, 20.867, 20.867]))
        self.assertEqual([[]], unique([[], [], [], []]))

    def test_two_items_list(self):
        self.assertEqual(['PardGaPoW', 'BonChon'], unique(['PardGaPoW', 'BonChon']))
        self.assertEqual([1000000, 2000000], unique([1000000, 2000000]))
        self.assertEqual([[], 'LIST'], unique([[], 'LIST', [], 'LIST']))

    def test_two_items_many_times_list(self):
        self.assertEqual(['SKE', 'CPE'], unique(['SKE', 'CPE', 'CPE', 'SKE']))
        self.assertEqual([33243, 88.6], unique([33243, 88.6, 33243, 88.6, 33243, 88.6, 33243, 88.6]))
        self.assertEqual([888, '1st'], unique([888, 888, '1st', 888, '1st', '1st', 888]))

    def test_many_items_list(self):
        self.assertEqual(['GOOD', 13.555, 10, []], unique(['GOOD', 13.555, 10, [], 10, 'GOOD', 13.555]))
        self.assertEqual([1122, 43454, 675 ,213 ,88655, 1435], unique([1122, 43454, 675, 213, 88655, 1435, 88655, 1122,
                                                                       675, 1435]))
        self.assertEqual(['PYTHON', 'IS', 'FUN', '?????'], unique(['PYTHON', 'IS', 'FUN', '?????', 'FUN', '?????', 'PYTHON']))

    def test_list_in_list(self):
        self.assertEqual([1, 3, 5, [2, 4, 6]], unique([1, 3, 5, [2, 4, 6]]))
        self.assertEqual([['FIVE'], [['HI']], ['THREE', 'O']], unique([['FIVE'], [['HI']], ['THREE', 'O']]))

    def test_many_lists_in_list(self):
        self.assertEqual([4000, [4], [900, 8]], unique([4000, [4], [900, 8]]))
        self.assertEqual([[[[]]], [1, 2, [3]]], unique([[[[]]], [1, 2, [3]]]))
        self.assertEqual(['STAR', [10000, ['WATERMALON', 'LEMON']], [3.00, 'I', ['U']]], unique(['STAR', [10000,['WATERMALON', 'LEMON']],
                                                                                       [3.00, 'I', ['U']]]))

    def test_large_list(self):
        self.assertEqual([1, 0, 7, 9], unique([1, 1, 1, 0, 7, 7, 9, 9, 9, 0, 0, 7, 1, 1, 1, 1,
                                               9, 9, 7, 1, 1, 0, 0, 9, 9, 1, 1, 7, 7, 7, 9, 0,
                                               7, 9, 9, 9, 0, 0, 7, 1, 7, 1, 1, 0, 0, 9, 9, 1,
                                               1, 1, 1, 0, 7, 7, 9, 9, 9, 0, 0, 7, 1, 1, 1, 1,
                                               9, 9, 7, 1, 1, 0, 0, 9, 9, 1, 1, 7, 7, 7, 9, 0,
                                               7, 9, 9, 9, 0, 0 ]))

    def test_type_error(self):
        with self.assertRaises(TypeError):
            unique('HI WORLD')
            unique('O')
            unique(98)
            unique(3.22)
            unique()
            unique(unique())

    def test_empty_list(self):
        self.assertEqual([], unique([]))

if __name__ == '__main__':
    unittest.main()