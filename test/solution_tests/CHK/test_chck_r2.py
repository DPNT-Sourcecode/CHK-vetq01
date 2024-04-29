import unittest
from lib.solutions.CHK.checkout_solution import checkout


class MyTestCase(unittest.TestCase):
    def test_product_with_mutiple_offers(self):
        skus = "AAAAAAAA"
        self.assertEqual(checkout(skus), 330)

    def test_product_with_invalid_product_offer(self):
        skus = "AAAEE"
        self.assertEqual(checkout(skus), 210)

    def test_product_with_valid_product_offer(self):
        skus = "AAAEEB"
        self.assertEqual(checkout(skus), 210)

    def test_product_with_multiple_instances(self):
        skus = "AAAAAAAAAA"
        self.assertEqual(checkout(skus), 400)

    def test_valid_offer_placement(self):
        skus = "A" * 15
        self.assertEqual(checkout(skus), 600)

    def test_valid_offer_placement(self):
        skus = "EEEEBB"
        self.assertEqual(checkout(skus), 160)

    def test_valid_offer_placement(self):
        skus = "BEBEEE"
        self.assertEqual(checkout(skus), 160)

    def test_valid_offer_placement(self):
        skus = "ABCDEABCDE"
        self.assertEqual(checkout(skus), 280)


if __name__ == '__main__':
    unittest.main()




