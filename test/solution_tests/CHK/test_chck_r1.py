import unittest
from lib.solutions.CHK.checkout_solution import checkout


class MyTestCase(unittest.TestCase):
    def test_without_offer(self):
        skus = "ABC"
        self.assertEqual(checkout(skus), 100)

    def test_with_offer(self):
        skus = "AAABCD"
        self.assertEqual(checkout(skus), 195)

    def test_with_invalid_product(self):
        skus = "AAAABCZ"
        self.assertEqual(checkout(skus), -1)

if __name__ == '__main__':
    unittest.main()
