'''
Created on Oct 8, 2012

@author: gsrinivasaraghavan
'''
import unittest
from random import randrange
from testgen_decorator import for_examples
import modheap

CMP_FUNCTION = lambda x, y : (1 if (x > y) else (-1 if (x < y) else 0))

class TestHeap(unittest.TestCase):

    def nlist(self, heapsize):
        '''
        Generate a random list of n numbers, each number is at most 2n
        '''
        lst = []
        randmax = 2*heapsize
        for _ in range(heapsize):
            lst.append(randrange(randmax))
        return lst

    @for_examples((True, 10, 1, 0, 1), (True, 20, 2, 3, 13), (True, 30, 3, 3, 25))
    @for_examples((False, 10, 1, 2, 5), (False, 15, 2, 2, 9), (False, 40, 3, 4, 33))
    def test_indices(self, ismin, heapsize, aexp, parent, child):
        '''
        Test max elements of the heap
        '''
        modheap.initialize_heap(ismin, aexp, CMP_FUNCTION)
        modheap.import_list(self.nlist(heapsize))
        self.assertEqual(child, modheap.get_leftmostchild_index(parent))
        self.assertEqual(parent, modheap.get_parent_index(child))


    @for_examples((True, 15, 2, 8, None), (False, 20, 3, 4, None))
    def test_nochild(self, ismin, heapsize, aexp, parent, child):
        '''
        Test if the functions correctly recognize leaves of the heap (those with no children)
        '''
        modheap.initialize_heap(ismin, aexp, CMP_FUNCTION)
        modheap.import_list(self.nlist(heapsize))
        self.assertEqual(child, modheap.get_leftmostchild_index(parent))


    @for_examples((False, 10, 1, None, 0), (True, 10, 2, None, 0))
    def test_noparent(self, ismin, heapsize, aexp, parent, child):
        '''
        Test if the functions correctly recognize the root of the heap (with no parent)
        '''
        modheap.initialize_heap(ismin, aexp, CMP_FUNCTION)
        modheap.import_list(self.nlist(heapsize))
        self.assertEqual(parent, modheap.get_parent_index(child))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()