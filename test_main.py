import unittest

from main import get_interval, swap_pos, s_sort


class MyTestCase(unittest.TestCase):
    def test_get_interval_6(self):
        self.assertEqual(get_interval(6), 3)

    def test_get_interval_8(self):
        self.assertEqual(get_interval(8), 4)

    def test_get_interval_9(self):
        self.assertEqual(get_interval(9), 4)

    def test_swap_pos(self):
        self.assertEqual(swap_pos([5, 3, 1], 0, 2), [1, 3, 5])

    def test_s_sort_of_len_3(self):
        self.assertEqual(s_sort([5, 3, 1]), [1, 3, 5])

    def test_s_sort_of_len_10(self):
        self.assertEqual(s_sort([4, 3, 2, 6, 10, 7, 9, 11, 8, 1]), [1, 2, 3, 4, 6, 7, 8, 9, 10, 11])


if __name__ == '__main__':
    unittest.main()
