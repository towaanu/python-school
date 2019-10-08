import unittest
from merge_sort import merge_sort

class TestMergeSort(unittest.TestCase):

    def test_merge_sort(self):
        list_to_sort = [38, 27, 43, 3, 9, 82, 10]
        self.assertListEqual(merge_sort(list_to_sort), [3, 9, 10, 27, 38, 43, 82])
    
    def test_random_merge_sort(self):
        list_to_sort = [1987, 127, 1, 56, 121, 5582, 98, 93, 100]
        self.assertListEqual(merge_sort(list_to_sort), [1, 56, 93, 98, 100, 121, 127, 1987, 5582])

if __name__ == '__main__':
    unittest.main()

