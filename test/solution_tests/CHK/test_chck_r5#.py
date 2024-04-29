import unittest
from lib.solutions.CHK.checkout_solution import checkout


class MyTestCase(unittest.TestCase):

    def test_invalid_deal(self):
        skus = "SSSTTT"
        self.assertEqual(checkout(skus), 120)

    def test_valid_deal(self):
        skus = "SSSTTTXXX"
        self.assertEqual(checkout(skus), 135)



if __name__ == '__main__':
    unittest.main()

