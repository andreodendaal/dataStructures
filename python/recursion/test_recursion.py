import recursion
import unittest


class TestRecursion(unittest.TestCase):
    def test_RecursionFunction(self):

        self.assertEqual(recursion.listSumRecursive([1, 3, 5, 7, 9]), 25)

        self.assertEqual(recursion.listSumRecursive([1]), 1)


if __name__ == '__main__':
    unittest.main(exit=False)
