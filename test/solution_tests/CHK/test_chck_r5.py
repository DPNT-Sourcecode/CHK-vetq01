import unittest
from lib.solutions.CHK.checkout_solution import checkout


class MyTestCase(unittest.TestCase):

    def test_invalid_deal(self):
        skus = "SSSTTT"
        self.assertEqual(checkout(skus), 90)

    def test_simple_deal(self):
        skus = "SSS"
        self.assertEqual(checkout(skus), 45)

    def test_valid_deal(self):
        skus = "SSSTTTXXX"
        self.assertEqual(checkout(skus), 135)

    def test_deal_with_one_extra_product(self):
        skus = "SSSZ"
        self.assertEqual(checkout(skus), 65)

    def test_valid_deal_with_mix(self):
        skus = "STTSSXXTX"
        self.assertEqual(checkout(skus), 135)



if __name__ == '__main__':
    unittest.main()



