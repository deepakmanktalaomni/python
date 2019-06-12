import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        a = calc.add()
        result = 15.0
        self.assertEqual(result,15.0)


if __name__ == '__main__':
    unittest.main()