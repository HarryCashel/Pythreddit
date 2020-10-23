import unittest
from src.main import add


class TestMathFunctions(unittest.TestCase):
    def test_add(self):
        result = add(1, 5)
        self.assertEqual(result, 6, msg="Add did not bring back 6 when given 1 and 5")

        result = add(0, 0)
        self.assertEqual(result, 0, msg="Add did not bring back 0 when given 0 and 0")

        result = add(-1, 1)
        self.assertEqual(result, 0, msg="Add did not bring back 0 when given -1 and 1")
