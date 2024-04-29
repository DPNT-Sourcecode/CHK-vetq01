import unittest
from lib.solutions.CHK.checkout_solution import checkout


class MyTestCase(unittest.TestCase):
    def test_product_with_mutiple_offers(self):
        skus = "AAAAAAAA"
        self.assertEqual(checkout(skus), 330)

    def test_product_with_product_offer(self):
        skus = "AAAEE"
        self.assertEqual(checkout(skus), 210)

    def test_product_with_multiple_instances(self):
        skus = "AAAAAAAAAA"
        self.assertEqual(checkout(skus), 400)

if __name__ == '__main__':
    unittest.main()


