import unittest
import lists

class TestLists(unittest.TestCase):
    def test_find_element(self):
        items = [43, 32, 111, 443, 45, 65, 76, 867]
        self.assertEqual((5, 65), lists.find_element(items, lambda x : x == 65))
    
    def test_max_element(self):
        items = [1, 43, 32, 111, 443, 45, 955, 65, 76, 867]
        self.assertEqual(955, lists.max_element(items))
    
    def test_min_element(self):
        items = [133, 43, 32, 111, 443, 955, 65, 1, 76, 867]
        self.assertEqual((7, 1), lists.min_element(items))
    
    def test_compute_avg(self):
        items = [16, 10, 88, 122]
        self.assertEqual(59, lists.compute_avg(items))

    def test_selection_sort(self):
        items = [65, 133, 16, 10, 88, 122, 22, 5]
        self.assertEqual([5, 10, 16, 22, 65, 88, 122, 133], lists.selection_sort(items))
    
    def test_insertion_sort(self):
        items = [65, 133, 16, 10, 88, 122, 22, 5]
        self.assertEqual([5, 10, 16, 22, 65, 88, 122, 133], lists.insertion_sort(items))

if __name__ == '__main__': 
    unittest.main()