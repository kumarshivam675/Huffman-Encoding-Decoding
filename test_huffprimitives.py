'''
Created on Oct 8, 2012

@author: gsrinivasaraghavan
'''
import os, unittest
from random import randrange
from testgen_decorator import for_examples
import modhuffman

class TestHuffman(unittest.TestCase):

    N_PRINTABLE_CHARS = 95
    FIRST_PRINTABLE_ORD = 32
    RANDOM_FILENAME = 'testcounts'

    def make_randomfile(self, filesize):
        '''
        Make a random file (with random characters) of a given size
        '''
        test_file = open(self.RANDOM_FILENAME, 'w')
        freq_table = {}
        for _ in range(filesize):
            randchar = chr(self.FIRST_PRINTABLE_ORD + randrange(self.N_PRINTABLE_CHARS))
            if (freq_table.has_key(randchar)):
                freq_table[randchar] += 1
            else:
                freq_table[randchar] = 1
            test_file.write(randchar)
        test_file.close()
        return freq_table

    @for_examples((1000), (15000), (5000))
    def test_freqtable(self, filesize):
        '''
        Test if the function 'build_char_table' is forming the correct hash, mapping characters occurring in a file
        to their frequencies
        '''
        freq_table = self.make_randomfile(filesize)
        built_freq_table = modhuffman.build_char_table(self.RANDOM_FILENAME)
        self.assertEqual(freq_table, built_freq_table)
        os.remove(self.RANDOM_FILENAME)

    @for_examples((1000, 1), (15000, 2), (5000, 3))
    def test_huffstack(self, filesize, arity_exp):
        '''
        Test max elements of the heap
        '''
        self.make_randomfile(filesize)
        freq_table = modhuffman.build_char_table(self.RANDOM_FILENAME)
        hufftree_hash = {}
        for char in freq_table:
            hufftree_hash[char] = [freq_table[char], 0, True]
        code_stack, root_symbol = modhuffman.build_huffman_tree(freq_table, arity_exp)
        last_freq = 0
        for tup in code_stack:
            char = tup[0]
            parent = tup[2]
            freq = tup[1]
            self.assertGreaterEqual(freq, last_freq)
            self.assertEqual(freq, hufftree_hash[char][0])
            if hufftree_hash.has_key(parent):
                hufftree_hash[parent][0] += freq
                hufftree_hash[parent][1] += 1
            else:
                hufftree_hash[parent] = [freq, 1, False]
            last_freq = freq
        for char in hufftree_hash:
            tup = hufftree_hash[char]
            self.assertTrue((tup[2] and tup[1] == 0) or (not tup[2] and tup[1] == 2))
        os.remove(self.RANDOM_FILENAME)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()