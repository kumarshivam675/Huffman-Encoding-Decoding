'''
Created on Sep 2, 2012

@author: gsrinivasaraghavan
'''
import unittest

__examples__ = "__examples__"

def for_examples(*examples):
    def decorator(f, examples=examples):
        setattr(f, __examples__, getattr(f, __examples__,()) + examples)
        return f
    return decorator

class TestCaseWithExamplesMetaclass(type):
    def __new__(meta, name, bases, dict):
        def tuplify(x):
            if not isinstance(x, tuple):
                return (x,)
            return x
        for methodname, method in dict.items():
            if hasattr(method, __examples__):
                dict.pop(methodname)
                examples = getattr(method, __examples__)
                delattr(method, __examples__)
                for example in (tuplify(x) for x in examples):
                    def method_for_example(self, method = method, example = example):
                        method(self, *example)
                    methodname_for_example = methodname + "(" + ", ".join(str(v) for v in example) + ")"
                    dict[methodname_for_example] = method_for_example
        
        return type.__new__(meta, name, bases, dict)

class TestCaseWithExamples(unittest.TestCase):
    __metaclass__ = TestCaseWithExamplesMetaclass
    pass

unittest.TestCase = TestCaseWithExamples