import unittest
# See PEP-0318 for motivation behind decorators
# See PEP-3129 for the rationale/semantics behind decorators

def sum(a, b):
    return a + b

def addOne(num):
    return num + 1

def decorateAddOne(func):
    def wrapper(a, b):
        # Note that this means decorator can only wrap
        # a function with exactly this signature (a, b)
        # Is it possible to make it generic?
        return func(a, b) + 1
    return wrapper

def decorateAddAny(c):
    def decorator(func):
        def wrapper(a, b):
            return func(a, b) + c
        return wrapper
    return decorator

@decorateAddOne
def sumDecorated(a, b):
    return a + b

@decorateAddOne
def multiplyDecorated(a, b):
    return a * b

@decorateAddAny(5)
def sumDecoratedAny(a, b):
    return a + b

'''
Goal achieved 
- to learn how to create an arbitrary decorator
- with arguments
- that can be applied to any function signature
'''
def decorateAddAnyGeneric(c):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) + c
        return wrapper
    return decorator

@decorateAddAnyGeneric(5)
def sumDecoratedGeneric(a, b, c):
    return a + b + c

@decorateAddAnyGeneric(4)
def multiplyDecoratedGeneric(a, b):
    return a * b

class TestDecorators(unittest.TestCase):
    def testSum(self):
        self.assertEqual(sum(2,3), 5)

    def testAddOne(self):
        self.assertEqual(addOne(5), 6)

    def testAddOneWrapper(self):
        self.assertEqual(addOne(sum(2,3)), 6)

    def testSumDecorated(self):
        # (2 + 3) + 1 = 6
        self.assertEqual(sumDecorated(2,3), 6)

    def testMultiplyDecorated(self):
        # (2 * 3) + 1 = 7
        self.assertEqual(multiplyDecorated(2,3), 7)

    def testSumDecoratedAny(self):
        # (2 + 3) + 5 = 10
        self.assertEqual(sumDecoratedAny(2,3), 10)

    def testSumDecoratedGeneric(self):
        # (1 + 2 + 3) + 5 = 11
        self.assertEqual(sumDecoratedGeneric(1,2,3), 10)

    def testMultiplyDecoratedGeneric(self):
        # (2*3) + 4 = 10
        self.assertEqual(multiplyDecoratedGeneric(2,3), 10)

if __name__ == '__main__':
    unittest.main()
