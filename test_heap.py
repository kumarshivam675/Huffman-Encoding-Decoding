'''
Created on Oct 8, 2012

@author: gsrinivasaraghavan
'''
import unittest
from testgen_decorator import for_examples
import modheap

CMP_FUNCTION = lambda x, y : (1 if (x > y) else (-1 if (x < y) else 0))

class TestHeap(unittest.TestCase):

    @for_examples(([2, 4, 1, 0, 9, 6]), ([9, 10, 4, 5, 20, 14, 13, 6, 8, 9]))
    def test_max(self, lst):
        '''
        Test max elements of the heap
        '''
        modheap.initialize_heap(False, 1, CMP_FUNCTION)
        modheap.import_list(lst)
        modheap.heapify()
        lst.sort()
        self.assertEqual(lst[-1], modheap.pop())
        self.assertEqual(lst[-2], modheap.pop())


    @for_examples(([2, 4, 1, 0, 9, 6]), ([9, 10, 4, 5, 20, 14, 13, 6, 8, 9]))
    def test_min(self, lst):
        '''
        Test min elements of the heap
        '''
        modheap.initialize_heap(True, 2, CMP_FUNCTION)
        modheap.import_list(lst)
        modheap.heapify()
        lst.sort()
        self.assertEqual(lst[0], modheap.pop())
        self.assertEqual(lst[1], modheap.pop())


    @for_examples(([2,4,1,0,9,6], 1), ([9,10,4,5,20,14,13,6,8,9], 2))
    def test_max_heap_sort(self, lst, exp2):
        '''
        Test max-heap sort
        '''
        modheap.initialize_heap(False, exp2, CMP_FUNCTION)
        for elem in lst:
            modheap.add(elem)
        lst.sort(reverse=True)
        sorted_list = []
        while (modheap.size() > 0):
            sorted_list.append(modheap.pop())
        self.assertEqual(lst, sorted_list)

    @for_examples(([8, 3, 5, 20, 16, 35, 15, 9, 18, 14], 1),
                  ([8, 3, 5, 20, 16, 35, 15, 9, 18, 14], 2))
    def test_min_heap_sort(self, lst, exp2):
        '''
        Test min-heap sort
        '''
        modheap.initialize_heap(True, exp2, CMP_FUNCTION)
        for elem in lst:
            modheap.add(elem)
        lst.sort()
        sorted_list = []
        while (modheap.size() > 0):
            sorted_list.append(modheap.pop())
        self.assertEqual(lst, sorted_list)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()