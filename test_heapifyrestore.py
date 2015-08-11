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


    def check_subtree_heap(self, i):
        '''
        Check if the subtree rooted at index i is a heap
        '''
        leftmost = modheap.get_leftmostchild_index(i)
        rightmost = modheap.get_rightmostchild_index(i)
        isheap = True
        if (leftmost != None):
            for j in range(leftmost, rightmost):
                if ((modheap.MIN_TOP and modheap.CMP_FUNCTION(modheap.get_item_at(j), modheap.get_item_at(i)) < 0) or
                    (not modheap.MIN_TOP and modheap.CMP_FUNCTION(modheap.get_item_at(j), modheap.get_item_at(i)) > 0)):
                    isheap = False
                    break
                else:
                    isheap = self.check_subtree_heap(j)
                    if not isheap:
                        break
        return isheap

    @for_examples((True, 10, 1), (True, 20, 2), (True, 30, 3))
    @for_examples((False, 10, 1), (False, 15, 2), (False, 40, 3))
    def test_restore_subtree(self, ismin, heapsize, aexp):
        '''
        Test if the heap property for a subtree rooted at a node can be restored, assuming the node was corrupted
        in an existing heap
        '''
        modheap.initialize_heap(ismin, aexp, CMP_FUNCTION)
        rlist = self.nlist(heapsize)
        modheap.import_list(rlist)
        modheap.heapify()
        i = randrange(len(rlist))
        modheap.DATA[i] = (min(rlist) - 1) if (ismin) else (max(rlist) + 1)
        modheap.restore_subtree(i)
        self.assertTrue(self.check_subtree_heap(i))
        

    @for_examples((True, 10, 1), (True, 20, 2), (True, 30, 3))
    @for_examples((False, 10, 1), (False, 15, 2), (False, 40, 3))
    def test_heapify(self, ismin, heapsize, aexp):
        '''
        Test Heapification
        '''
        modheap.initialize_heap(ismin, aexp, CMP_FUNCTION)
        modheap.import_list(self.nlist(heapsize))
        modheap.heapify()
        self.assertTrue(self.check_subtree_heap(0))


    @for_examples((True, 10, 1), (True, 20, 2), (True, 30, 3))
    @for_examples((False, 10, 1), (False, 15, 2), (False, 40, 3))
    def test_restore_heap(self, ismin, heapsize, aexp):
        '''
        Test if the heap is restored correctly after a single-node gets corrupted
        '''
        modheap.initialize_heap(ismin, aexp, CMP_FUNCTION)
        rlist = self.nlist(heapsize)
        modheap.import_list(rlist)
        modheap.heapify()
        i = randrange(len(rlist))
        modheap.DATA[i] = (min(rlist) - 1) if (not ismin) else (max(rlist) + 1)
        modheap.restore_heap(i)
        self.assertTrue(self.check_subtree_heap(i))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()