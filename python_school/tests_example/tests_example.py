import unittest

def plus(a: int, b: int) -> int:
    """ A simple function summing two numbers
    >>> plus(4, 9)
    13
    >>> plus(10, 20)
    30
    """
    return a + b


class TestPlus(unittest.TestCase):

    def test_plus(self):
        self.assertEqual(plus(10, 11), 21, "Should be 21")

if __name__ == '__main__':
    import doctest
    help(plus)
    input('doctest.testmod()')
    doctest.testmod()
    input('unittest.main()')
    unittest.main()

