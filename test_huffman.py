'''
Created on Oct 31, 2012

@author: gsrinivasaraghavan
'''
import unittest
import filecmp
import os
from testgen_decorator import for_examples
from modhuffman import compress, uncompress

class TestHuffman(unittest.TestCase):

    @for_examples(("text1", 370), ("text2", 5900), ("text3", 19500))
    def test_compression(self, original_file, compressed_size):
        '''
        Test max elements of the heap
        '''
        compressed_file = compress(original_file, 1)
        self.assertLessEqual(os.path.getsize(compressed_file), compressed_size)
        recovered_file = uncompress(compressed_file)
        self.assertNotEqual(original_file, recovered_file)
        self.assertEqual(os.path.getsize(original_file), os.path.getsize(recovered_file))
        self.assertEqual(True, filecmp.cmp(original_file, recovered_file))

if __name__ == "__main__":
    import sys;sys.argv = ['', 'Test.testName']
    unittest.main()