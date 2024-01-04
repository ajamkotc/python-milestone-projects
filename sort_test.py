import unittest
import random
import sort

class TestSorts(unittest.TestCase):
    '''Test suite for sorting methods.

    Methods
    -------
    test_merge_lists
        Tests class method merge_lists.
    test_merge_lists2
        Tests class method merge_lists.
    test_bubble_sort
        Tests class method bubble_sort'''

    def test_merge_lists(self):
        '''Tests class method merge_lists.'''

        # Create two random lists of random length
        list_length = random.randint(100, 200)
        random_list = random.sample(range(1, list_length), list_length - 1)
        list2_length = random.randint(100, 200)
        random_list2 = random.sample(range(1, list2_length), list2_length - 1)

        # Sort them individually since method is meant to be used with sorted lists
        random_list.sort()
        random_list2.sort()

        merged_list = sort.Sort.merge_lists(random_list, random_list2)

        # Create test case by using built in sort method
        test_list = random_list + random_list2
        test_list.sort()

        self.assertEqual(merged_list, test_list, 'Lists not merged correctly.')

    def test_merge_sort(self):
        '''Tests merge-sort algorithm.'''

        list_length = random.randint(100, 200)
        random_list = random.sample(range(1, list_length), list_length - 1)

        merge_sorted = sort.Sort.merge_sort(random_list)
        random_list.sort()

        self.assertEqual(merge_sorted, random_list, 'Merge sort incorrect.')

    def test_bubble_sort(self):
        '''Tests class method bubble_sort.'''

        list_length = random.randint(100, 200)
        random_list = random.sample(range(1, list_length), list_length - 1)

        bubble_sorted = sort.Sort.bubble_sort(random_list)
        random_list.sort()

        self.assertEqual(bubble_sorted, random_list, "Bubble sort doesn't work.")

if __name__ == '__main__':
    unittest.main()