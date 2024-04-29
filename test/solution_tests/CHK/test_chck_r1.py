import unittest
from lib.solutions.CHK.checkout_solution import checkout


class MyTestCase(unittest.TestCase):
    def test_without_offer(self):
        skus = "ABC"
        self.assertEqual(checkout(skus), 100)

    def test_without_offer_2(self):
        skus = "AABCD"
        self.assertEqual(checkout(skus), 165)

    def test_with_offer(self):
        skus = "AAABCD"
        self.assertEqual(checkout(skus), 195)

    def test_with_invalid_product(self):
        skus = "AAAABCZ"
        self.assertEqual(checkout(skus), -1)

    def test_with_multiple_of_one_product(self):
        skus = "AAAA"
        self.assertEqual(checkout(skus), 180)

    def test_with_multiple_of_varied_products(self):
        skus = "AAAABBBBB"
        self.assertEqual(checkout(skus), 600)

if __name__ == '__main__':
    unittest.main()

